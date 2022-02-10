from django.contrib.auth.models import User
from django.shortcuts import render
from photos.models import Photo

# Create your views here.


def home(request):
    photos = Photo.objects.all()

    return render(request,'home.html',context={'photo':photos})

def publicProfile(request,user):
    try:
        user = User.objects.get(username=user)
        photos = Photo.objects.filter(user=user)
    except:
        pass
    return render(request,'public-profile.html',context={'users':user,'photo':photos})