from django.urls import path
from .import views


urlpatterns = [
    path('join/',views.joinAPIView.as_view(),name="JoinAPIView"),
    path('login/', views.MyTokenObtainPairView.as_view(), name='LoginAPIView'),
    path('user/<str:user>/',views.UserAPIView.as_view(),name="UserAPIView"),
    path('profile/<str:user>/',views.ProfileAPIView.as_view(),name="ProfileAPIView"),
    path('profile/',views.AllProfileAPIView.as_view(),name="AllProfileAPIView"),
    path('change-password/<str:user>/',views.ChangePasswordAPIView.as_view(),name="ChangePasswordAPIView"),
    path('photo/',views.PhotoAPIView.as_view(),name="PhotoAPIView"),
    path('photo/<str:user>/',views.UserPhotoAPIView.as_view(),name="UserPhotoAPIView"),
    path('photo/download/counts/',views.PhotoDownloadCountAPIView.as_view(),name="PhotoDownloadCountAPIView"),
    path('photo/download/count/<int:id>/',views.PhotoDownloadAPIView.as_view(),name="PhotoDownloadAPIView")
]
