from django.shortcuts import render,redirect
#from bs4 import BeautifulSoup
from requests import get
import json
from django.http import HttpResponse
from accounts.models import profile
from django.contrib.auth.models import User
def view_profile(request,token):
    if not User.objects.filter(username=token).exists():
        return render(request,'404.html')
    user_obj=profile.objects.filter(user=token)[0]
    lc1=None
    lc2=None
    cc=None
    cf=None
    context={}
    if user_obj.codechef_verified:
        t=codechef(user_obj.codechef)
        if t :
            context['cc']=[user_obj.codechef,t,None]
        
    if user_obj.codeforces_verified:
        t=codeforces(user_obj.codeforces)
        if t:
            context['cf']=[user_obj.codeforces,t]
        
    if user_obj.leetcode_verified:
        lc2=leetcode2(user_obj.leetcode)
        if lc2:
            context['lc']=[user_obj.leetcode,None,lc2]
    if user_obj.institute!="@ Not Available":
        context['institute']=user_obj.institute
    context['email']=user_obj.email
    context['follower']=user_obj.followers
    context['first_name']=user_obj.first_name
    context['last_name']=user_obj.last_name
    context['user']=token
    print(token,request.user,request.user.is_authenticated)
    if request.user.is_authenticated:

        if str(request.user)==token:
            context['addfriend']=3
        else:
            curr_obj=profile.objects.filter(user=request.user)[0].friends
            if token in curr_obj:
                context['addfriend']=2
            else:
                context['addfriend']=1
    else:
        context['addfriend']=1
    return render(request,'profile.html',context)
def codechef(user_name):
    url="https://codechef-api.vercel.app/"+str(user_name)
    r=get(url)
    if r.status_code == 200:
        j=json.loads(r.text)
        return j
    return False
def codeforces(user_name):
    url="https://codeforces.com/api/user.info?handles="+str(user_name)
    r=get(url)
    if r.status_code == 200:
        j=json.loads(r.text)
        if j['status']=='OK':
            return j
    return False

def leetcode2(user):
    url = 'https://leetcode.com/graphql?query=query%20{%20userContestRanking(username:%20%22' + user + '%22)%20{%20attendedContestsCount%20rating%20globalRanking%20totalParticipants%20topPercentage%20}}'
    r=get(url)
    if r.status_code == 200:
        j=json.loads(r.text)
        return j
    return False

def leaderboard(request,token):
    if "@" not in token:
        user_obj=profile.objects.filter(institute=token)
        friends=[]
        for x in user_obj:
            friends.append(x.user)
        context={}
        context['friends']=[]
        for friend in friends:
            user_obj=profile.objects.filter(user=friend)[0]
            t=[friend]
            if user_obj.leetcode_verified:
                lc=leetcode2(user_obj.leetcode)
                if lc:
                    try:
                        y=int(lc['data']['userContestRanking']['rating'])
                    except Exception as e:
                        y="-"
                    t.append(y)
                else:
                    t.append("-")
            else:
                t.append("-")
            if user_obj.codechef_verified:
                cc=codechef(user_obj.codechef)
                if cc:
                    try:
                        y=int(cc['currentRating'])
                    except Exception as e:
                        y="-"
                    t.append(y)
                else:
                    t.append("-")
            else:
                t.append("-")
            if user_obj.codeforces_verified:
                cf=codeforces(user_obj.codeforces)
                if cf:
                    try:
                        y=int(cf['result'][0]['rating'])
                    except Exception as e:
                        y="-"
                    t.append(y)
                else:
                    t.append("-")
            else:
                t.append("-")
            context['friends'].append(t)
        context['friends']=json.dumps(context['friends'])
        return render(request,'leaderboard.html',context)
    if not request.user.is_authenticated:
        return render(request,'leaderboard.html',{'friends':json.dumps([])})
    user_obj=profile.objects.filter(user=request.user)[0]
    friends=user_obj.friends
    context={}
    context['friends']=[]
    for friend in friends:
        user_obj=profile.objects.filter(user=friend)[0]
        t=[friend]
        if user_obj.leetcode_verified:
            lc=leetcode2(user_obj.leetcode)
            if lc:
                try:
                    y=int(lc['data']['userContestRanking']['rating'])
                except Exception as e:
                    y="-"
                t.append(y)
            else:
                t.append("-")
        if user_obj.codechef_verified:
            cc=codechef(user_obj.codechef)
            if cc:
                try:
                    y=int(cc['currentRating'])
                except Exception as e:
                    y="-"
                t.append(y)
            else:
                t.append("-")
        if user_obj.codeforces_verified:
            cf=codeforces(user_obj.codeforces)
            if cf:
                try:
                    y=int(cf['result'][0]['rating'])
                except Exception as e:
                    y="-"
                t.append(y)
            else:
                t.append("-")
        
        context['friends'].append(t)
    context['friends']=json.dumps(context['friends'])
    return render(request,'leaderboard.html',context)
def alter_friend(request,token):
    if not request.user.is_authenticated:
        return render(request,'404.html')
    if request.user==token:
        return render(request,'404.html')
    else:
        curr_obj=profile.objects.filter(user=request.user)[0]
        user_obj=profile.objects.filter(user=token)[0]
        if token in curr_obj.friends:
            curr_obj.friends.pop(token)
            user_obj.followers-=1
        else:
            curr_obj.friends[token]=1
            user_obj.followers+=1
        curr_obj.save()
        user_obj.save()
        return redirect('/accounts/profile/'+token)
            
