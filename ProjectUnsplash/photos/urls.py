from django.urls import path
from .import views

urlpatterns = [
    path('submit/',views.submitPhoto,name="submitPhoto")
]
