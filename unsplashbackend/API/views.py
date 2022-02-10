from rest_framework.response import Response
from .serializers import JoinSerializer, PhotoDownloadSerializer,ProfileSerializer,PhotoSerializer,PhotosDownload
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status
from .models import Profile, Photo, PhotosDownload
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from django.contrib.auth import authenticate

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        return data
        

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class joinAPIView(APIView):
    def post(self,request):
        data = request.data
        serializer = JoinSerializer(data=data)
        if serializer.is_valid():
            User.objects.create(
                username = data['username'],
                email = data['email'],
                first_name = data['first_name'],
                last_name = data['last_name'],
                password = make_password(data['password'])
            )
            msg = {'success':"Join Sucessfully"}
            return Response(msg,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,user):
        data = User.objects.get(username=user)
        serializers = JoinSerializer(data)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    def patch(self,request,user):
        data = request.data
        u = User.objects.get(username=user)
        serializers = ProfileSerializer(u,data=data,partial=True)
        if serializers.is_valid():
            usr = User.objects.get(username=u)
            usr.first_name = data['first_name']
            usr.last_name = data['last_name']
            usr.save()
            msg = {'updated':"Account Updated"}
            return Response(msg,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_403_FORBIDDEN)

    def delete(self,request,user):
        password = request.data['password']
        auth = authenticate(request,username=user,password=password)
        if auth is not None:
            User.objects.get(username=user).delete()
            msg = {'Deleted':"Account Deleted"}
            return Response(msg,status=status.HTTP_200_OK)
        else:
            msg = {'password':"Invalid Password"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)


            
class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    def get(self,request,user):
        u = User.objects.get(username=user)
        data = Profile.objects.get(user=u)
        serializers = ProfileSerializer(data)
        return Response(serializers.data,status=status.HTTP_200_OK)
    def patch(self,request,user):
        data = request.data
        u = User.objects.get(username=user)
        u_id = Profile.objects.get(user=u)
        serializers = ProfileSerializer(u_id,data=data,partial=True)
        if serializers.is_valid():
            serializers.save()
            msg = {'updated':"Account Updated"}
            return Response(msg,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_403_FORBIDDEN)

    
class AllProfileAPIView(APIView):
    def get(self,request):
        data = Profile.objects.all()
        serializer = ProfileSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

        

class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,user):
        data = request.data
        op = data['old_password']
        np = data['new_password']
        cp = data['confirm_password']
        print(data)
        if op == '':
            return Response({'old_password':'This field may not be blank.'})
        elif np == '':
            return Response({'new_password':'This field may not be blank.'})
        elif cp == '':
            return Response({'confirm_password':'This field may not be blank.'})
        else:
            user = authenticate(request,username=user,password=op)
            if user is not None:
                if np == cp:
                    u = User.objects.get(username=user)
                    u.password = make_password(np)
                    u.save()
                    return Response({'Success':'Password Updated Successfully'})
                else:
                    return Response({'Failed':'Two password did not matched'})
            else:
                return Response({'old_password':'Old password did not matched.'})


class PhotoAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    def post(self,request):
        print(request.data)
        data = request.data
        u = User.objects.get(username=data['user'])
        serializer = PhotoSerializer(u,data=data)
        if serializer.is_valid():
            Photo.objects.create(
                user = u,
                image = data['image'],
                tags = data['tags'],
                desc = data['desc']
            )
            msg = {'success':'Photo uploaded'}
            return Response(msg,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        data = Photo.objects.all()
        serializer = PhotoSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)




class UserPhotoAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,user):
        u = User.objects.get(username=user)
        data = Photo.objects.filter(user=u)
        serializer = PhotoSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class PhotoDownloadCountAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        data = PhotosDownload.objects.all()
        serializer = PhotoDownloadSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_100_CONTINUE)

class PhotoDownloadAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,id):
        photo_id = Photo.objects.get(id=id)
        download = PhotosDownload.objects.get(photo=photo_id)
        download.count += 1
        download.save()
        return Response(status=status.HTTP_200_OK)

