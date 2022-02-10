from django.urls import path
from .import views
from django.contrib.auth import views as authview

urlpatterns = [
    path('login/',views.Login,name="login"),
    path('join/',views.join,name="join"),
    path('logout/',authview.LogoutView.as_view(template_name='logout.html'),name="logout"),
    path('edit-profile/',views.editProfile,name="editProfile"),
    path('change-password/',views.changePassword,name="changePassword"),
    path('close/',views.closeAccount,name="closeAccount"),
    path('download-history/',views.downloadHistroy,name='downloadHistory')
]
