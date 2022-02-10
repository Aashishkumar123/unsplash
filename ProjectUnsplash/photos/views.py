from django.shortcuts import render
from .models import Photo
from django.contrib.auth.decorators import login_required

@login_required
def submitPhoto(request):
    if request.method == "POST":
        photo = 'photos' in request.FILES and request.FILES['photos']
        tag = 'tag' in request.POST and request.POST['tag']
        decs ='decs' in request.POST and request.POST['decs']

        Photo.objects.create(
                user = request.user,
                image = photo,
                tags = tag,
                desc = decs
        )
        model = True
        return render(request,'submit-photo.html',context={'model':model})
    model = False
    return render(request,'submit-photo.html',context={'model':model})