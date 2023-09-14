from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from accounts.models import profile
from django.core.mail import send_mail
import uuid
def about(request):
    return render(request,'about.html')
def home(request):
    return render(request,'home.html')
def log_in(request):
    if request.user.is_authenticated:
            return render(request,'404.html')
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            context={'greenalert':"login successful"}
            return render(request,'home.html',context)
        if User.objects.filter(username=username).exists():
            context={'redalert':"wrong password"}
            return render(request,'login.html',context)
        context={'redalert':"User name doesn't exist"}
        return render(request,'login.html',context)
    else:
        return render(request,'login.html')
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        context={'greenalert':"logout successful"}
        return render(request,'home.html',context)
    return render(request,'404.html')
def register_page(request):
    if request.user.is_authenticated:
            return render(request,'404.html')
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        if " " in username or "@" in username:
            context={'redalert':'username should not contain spaces and @'}
            return render(request,'register.html',context)
        user_obj = profile.objects.filter(email = email)
        if User.objects.filter(username=username).exists() or profile.objects.filter(user=username).exists():
            context={'redalert':'username already taken'}
            return render(request,'register.html',context)
        if user_obj.exists() :
            user_obj=user_obj[0]
            if user_obj.email_verified==True:
                context={'redalert':'email already taken'}
                return render(request,'register.html',context)
            else:
                user_obj.user=username
                user_obj.first_name = first_name
                user_obj.last_name= last_name
                user_obj.save()
                
        else:
            profile.objects.create(first_name = first_name , last_name= last_name , email = email , user =username)
        try:
            send_verification_mail(request,email)
            context={'greenalert':'verification email sent'}
            return render(request,'register.html',context)
        except Exception as e:
            context={'redalert':'Something went wrong, try again'}
            return render(request,'register.html',context)
    return render(request,'register.html')


def set_password(request,token):
    t=token.split("@")
    if len(t)!=2:
        return render(request,'404.html')
    user,token=t[0],t[1]
    if token=="Not Available":
        return render(request,'404.html')
    user_obj=profile.objects.filter(user=user)
    if not user_obj.exists():
        return render(request,'404.html')
    if request.method=='POST':
        user_obj=user_obj[0]
        if user_obj.token==token:
            if User.objects.filter(username=user).exists():
                t=User.objects.get(username=user)
                t.set_password(request.POST.get('password'))
                t.save()
                user_obj.token="Not Available"
                user_obj.save()
                context={'greenalert':"password changed successfully"}
                return render(request,'set_password.html',context)
            else:
                t=User.objects.create(username=user)
                t.set_password(request.POST.get('password'))
                t.save()
                user_obj.token="Not Available"
                user_obj.email_verified=True
                user_obj.friends[user]=1
                user_obj.save()
                context={'greenalert':"Account created successfully"}
                return render(request,'set_password.html',context)
        else:
            return render(request,'404.html')
    else:
        user_obj=user_obj[0]
        if user_obj.token==token:
            return render(request,'set_password.html')
        else:
            return render(request,'404.html')
        
def send_verification_mail(request,email):
    user_obj = profile.objects.filter(email = email)[0]
    user_obj.token = str(uuid.uuid4())
    user_obj.save()
    scheme = request.scheme
    domain_name = request.get_host()
    url = f"{scheme}://{domain_name}"
    url+="/password/"+user_obj.user+"@"+user_obj.token
    send_mail(
        'Verify your codetrack account',
        'Click the link to verify your codetrack account and set password  \n'+url+'\n ',
        'codetrack.co@gmail.com',
        [email],
        fail_silently=False,
    )
def forget_password(request):
    if request.method=="POST":
        email=request.POST['email']
        if profile.objects.filter(email=email).exists():
            send_verification_mail(request,email)
            context={'greenalert':"reset mail  sent"}
            return render(request,'forget_password.html',context)
        else:
            context={'redalert':"invalid email"}
            return render(request,'forget_password.html',context)
    else:
        return render(request,'forget_password.html')
    
def forget_username(request):
    if request.method=="POST":
        email=request.POST['email']
        if profile.objects.filter(email=email).exists():
            username=profile.objects.filter(email=email)[0].user
            context={'greenalert':"Username : "+username}
            return render(request,'forget_username.html',context)
        else:
            context={'redalert':"invalid email"}
            return render(request,'forget_username.html',context)
    else:
        return render(request,'forget_username.html')