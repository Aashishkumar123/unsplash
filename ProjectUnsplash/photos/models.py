from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'Photos')
    tags = models.CharField(max_length=200, blank=True)
    desc = models.TextField(max_length=500, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
