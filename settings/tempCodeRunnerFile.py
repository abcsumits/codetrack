from requests import get
from bs4 import BeautifulSoup
import json
from django.shortcuts import render,redirect
from accounts.models import profile
from django.http import HttpResponse 
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
import uuid

def settings(request):
    if not request.user.is_authenticated:
        return render(request,'404.html')
    return render(request,'setting.html')

def change_institute(request):
    if not request.user.is_authenticated:
        return render(request,'404.html')
    if request.method=='POST':
        if "@" in request.POST['institute']:
            context={'redalert':'Institute name should not contain @'}
            return render(request,'institute.html',context)
        user_obj=profile.objects.filter(user=request.user)[0]
        user_obj.institute=request.POST['institute']
        user_obj.save()
        context={'greenalert':'Changed institute name successfully'}
        return render(request,'setting.html',context)
    context={}
    r=profile.objects.filter(user=request.user)[0]
    if "@" not in  r.institute:
        context['institute']=r.institute
    return render(request,'institute.html',context)
def leetcode_name(request):
    if not request.user.is_authenticated:
        return render(request,'404.html')
    if request.method =='POST':
        username=request.POST['username']
        j=leetcode(username)
        if j==False:
            context={'redalert':'Check the entered username'}
            return render(request,'leetcode_name.html',context)
        user_obj=profile.objects.filter(user=request.user)[0]
        user_obj.leetcode=username
        user_obj.leetcode_verified=False
        t=str(uuid.uuid4()).split("-")
        user_obj.leetcode_token="lc"+"".join(t)[:28]
        
        user_obj.save()
        return redirect('/settings/leetcode_check/')
    r=profile.objects.filter(user=request.user)[0]
    context={}
    if r.leetcode_verified:
        context['leetcode']=r.leetcode
    return render(request,'leetcode_name.html',context)
def leetcode_check(request):
    if not request.user.is_authenticated:
        return render(request,'404.html')
    user_obj=profile.objects.filter(user=request.user)[0]
    if user_obj.leetcode_token=="Not Available":
        return render(request,'404.html')
    if request.method =='POST':
        j=leetcode(user_obj.leetcode)
        if j['name']==user_obj.leetcode_token:
            user_obj.leetcode_token="Not Available"
            user_obj.leetcode_verified=True
            user_obj.save()
            context={'greenalert':'account added successfully'}
            return render(request,'setting.html',context)
        else:
            context={'redalert':'Name does not matched ,Try again.','username':user_obj.leetcode,'token':user_obj.leetcode_token}
            return render(request,'leetcode_check.html',context)
    context={'username':user_obj.leetcode,'token':user_obj.leetcode_token}
    return render(request,'leetcode_check.html',context)
def leetcode(user_name):
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    url="https://leetcode.com/"+str(user_name)
    r=get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    r=soup.find_all("script")[0]
    if len(r)==0:
        return False
    j=json.loads(r.text)
    return j#["name"]
def codechef_name(request):
    if not request.user.is_authenticated:
        return render(request,'404.html')
    if request.method =='POST':
        username=request.POST['username']
        j=codechef(username)
        if j==False:
            context={'redalert':'Check the entered username'}
            return render(request,'codechef_name.html',context)
        user_obj=profile.objects.filter(user=request.user)[0]
        user_obj.codechef=username
        user_obj.codechef_verified=False
        t=str(uuid.uuid4()).split("-")
        user_obj.codechef_token="cc"+"".join(t)[:28]
        
        user_obj.save()
        return redirect('/settings/codechef_check/')
    r=profile.objects.filter(user=request.user)[0]
    context={}
    if r.codechef_verified:
        context['codechef']=r.codechef
    return render(request,'codechef_name.html',context)
def codechef_check(request):
    if not request.user.is_authenticated:
        return render(request,'404.html')
    user_obj=profile.objects.filter(user=request.user)[0]
    if user_obj.codechef_token=="Not Available":
        return render(request,'404.html')
    if request.method =='POST':
        j=codechef(user_obj.codechef)
        if j==user_obj.codechef_token:
            user_obj.codechef_token="Not Available"
            user_obj.codechef_verified=True
            user_obj.save()
            context={'greenalert':'account added successfully'}
            return render(request,'setting.html',context)
        else:
            context={'redalert':'Name does not matched ,Try again.','username':user_obj.codechef,'token':user_obj.codechef_token}
            return render(request,'codechef_check.html',context)
    context={'username':user_obj.codechef,'token':user_obj.codechef_token}
    return render(request,'codechef_check.html',context)
def codechef(user_name):
    url="https://codechef-api.vercel.app"+str(user_name)
    r=get(url)
    if r.status_code == 200:
        j=json.loads(r.text)
        return j['name']
    return False
def codeforces_name(request):
    if not request.user.is_authenticated:
        return render(request,'404.html')
    if request.method =='POST':
        username=request.POST['username']
        j=codeforces(username)
        if j==False:
            context={'redalert':'Check the entered username'}
            return render(request,'codeforces_name.html',context)
        user_obj=profile.objects.filter(user=request.user)[0]
        user_obj.codeforces=username
        user_obj.codeforces_verified=False
        user_obj.codeforces_token="cf"+"".join(str(uuid.uuid4()).split("-"))[:28]
        user_obj.save()
        return redirect('/settings/codeforces_check/')
    r=profile.objects.filter(user=request.user)[0]
    context={}
    if r.codeforces_verified:
        context['codeforces']=r.codeforces
    return render(request,'codeforces_name.html',context)
def codeforces_check(request):
    if not request.user.is_authenticated:
        return render(request,'404.html')
    user_obj=profile.objects.filter(user=request.user)[0]
    if user_obj.codeforces_token=="Not Available":
        return render(request,'404.html')
    if request.method =='POST':
        j=codeforces(user_obj.codeforces)
        if j==user_obj.codeforces_token:
            user_obj.codeforces_token="Not Available"
            user_obj.codeforces_verified=True
            user_obj.save()
            context={'greenalert':'account added successfully'}
            return render(request,'setting.html',context)
        else:
            context={'username':user_obj.codeforces,'token':user_obj.codeforces_token,'redalert':'Name does not matched ,Try again.'}
            return render(request,'codeforces_check.html',context)
    context={'username':user_obj.codeforces,'token':user_obj.codeforces_token}
    return render(request,'codeforces_check.html',context)
def codeforces(user_name):
    url="https://codeforces.com/api/user.info?handles="+str(user_name)
    r=get(url)
    if r.status_code == 200:
        j=json.loads(r.text)
        if j['status']=='OK':
            return j['result'][0]['firstName']
    return False