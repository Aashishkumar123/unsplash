from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile')
    location = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    site = models.URLField(blank=True)
    interest = models.TextField(max_length=300, blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    paypal = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return str(self.user)


class Photo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    image = models.ImageField(upload_to = 'Photos')
    tags = models.CharField(max_length=200, blank=True)
    desc = models.TextField(max_length=500, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class PhotosDownload(models.Model):
    photo = models.OneToOneField(Photo,on_delete=models.CASCADE)
    count = models.IntegerField(default=0,blank=False)

