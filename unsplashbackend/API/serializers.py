from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class JoinSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField()

    class Meta:
        model = Profile
        fields = ['user','image','location','bio','site','interest','instagram','twitter','paypal']

class PhotoSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    
    class Meta:
        model = Photo
        fields = ['id','user','image','tags','desc','datetime']

class PhotoDownloadSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhotosDownload
        fields = ['photo','count']