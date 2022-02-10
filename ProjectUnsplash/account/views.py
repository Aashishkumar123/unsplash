from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def Login(request):
    if request.method == "POST" and 'login' in request.POST:
        uname = 'uname' in request.POST and request.POST['uname']
        pwd = 'pwd' in request.POST and request.POST['pwd']

        user = authenticate(request,username=uname,password=pwd)
        
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'username or password is invalid')

    return render(request,'login.html')

def join(request):
    if request.method == "POST" and 'join' in request.POST:
        fname = 'fname' in request.POST and request.POST['fname']
        lname = 'lname' in request.POST and request.POST['lname']
        em = 'email' in request.POST and request.POST['email']
        uname = 'uname' in request.POST and request.POST['uname']
        pwd = 'pwd' in request.POST and request.POST['pwd']

        if User.objects.filter(email=em).exists():
            messages.error(request,'This email address is already exists')
        
        elif User.objects.filter(username=uname).exists():
            messages.error(request,'This Username is already exists')

        elif len(uname) <= 6:
            messages.error(request,'Username should have more than 6 charcters')

        elif len(pwd) <= 8:
            messages.error(request,'password should have more than 8 charcters')
        
        else:
            User.objects.create(
                username = uname,
                first_name = fname,
                last_name = lname,
                email = em,
                password = make_password(pwd)
                
            )
            messages.success(request,'Joined Successfully')



    return render(request,'join.html')

@login_required
def editProfile(request):
    if request.method == "POST" and 'update' in request.POST:
        fname = 'fname' in request.POST and request.POST['fname']
        lname = 'lname' in request.POST and request.POST['lname']
        em = 'em' in request.POST and request.POST['em']
        img = 'img' in request.FILES and request.FILES['img']
        loc = 'loc' in request.POST and request.POST['loc']
        bios = 'bio' in request.POST and request.POST['bio']
        sites = 'site' in request.POST and request.POST['site']
        inter = 'inter' in request.POST and request.POST['inter']
        insta = 'insta' in request.POST and request.POST['insta']
        twitt = 'twitt' in request.POST and request.POST['twitt']
        paypl = 'paypl' in request.POST and request.POST['paypl']

        u = User.objects.get(username=request.user)
        u.first_name = fname
        u.last_name = lname
        u.email = em

        profile = Profile.objects.get(user=request.user)
        if img is not False:
            profile.image = img
        profile.location = loc
        profile.bio = bios
        profile.site = sites
        profile.interest = inter
        profile.instagram = insta
        profile.twitter = twitt
        profile.paypal = paypl
        u.save()
        profile.save()
        messages.success(request,'Account Updated')

    return render(request,'edit-profile.html')

@login_required
def changePassword(request):
    if request.method == "POST" and 'update_pwd' in request.POST:
        old_pwd = 'old_pwd' in request.POST and request.POST['old_pwd']
        new_pwd = 'new_pwd' in request.POST and request.POST['new_pwd']
        crfm_pwd = 'crfm_pwd' in request.POST and request.POST['crfm_pwd']

        pass_auth = authenticate(request,username=request.user,password=old_pwd)
        if pass_auth is not None:
            if len(new_pwd) <= 8:
                messages.error(request,'New password should have more than 8 charcters')
            elif old_pwd == new_pwd:
                messages.error(request,'New password should not matched with old password')
            elif new_pwd != crfm_pwd:
                messages.error(request,'Two password did not matched')
            else:
                u = User.objects.get(username=request.user)
                u.password = make_password(new_pwd)
                u.save()
                messages.success(request,'Password updated successfully')
        else:
            messages.error(request,'Old password did not match')
    return render(request,'change-password.html')

login_required
def closeAccount(request):
    if request.method =="POST":
        # pwd = 'pwd' in request.POST and request.POST['pwd']
        # pass_auth = authenticate(request,username=request.user,password=pwd)
        # if pass_auth is not None:
        #     User.objects.get(username=request.user).delete()
        # else:
        #     messages.error(request,'Wrong password')
        print('submit')


    return render(request,'close-account.html')

login_required
def downloadHistroy(request):
    return render(request,'download-history.html')