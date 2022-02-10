from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','image','location','bio','site','interest','instagram','twitter','paypal']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','user','image','tags','desc','datetime']

@admin.register(PhotosDownload)
class PhotoDownloadAdmin(admin.ModelAdmin):
    list_display = ['photo','count']
    
