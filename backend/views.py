from django.shortcuts import render
import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework import permissions
from rest_framework import generics,filters
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.conf import settings
from rest_framework.filters import SearchFilter
from datetime import datetime, timedelta
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Register
from .serializer import Register_serilizer
from .models import Posts,Comments,Likes,Follow
from .serializer import comments_serilizer,posts_serilizer,likes_serilizer,follow_serilizer
 

# ___________________ register________

class Register_list(ListCreateAPIView):
    queryset=Register.objects.all()
    serializer_class=Register_serilizer
    permission_classes=[permissions.AllowAny]



# _________________________ Social Media API ________________________________
class Postslistview(generics.ListCreateAPIView):
    queryset=Posts.objects.all().order_by('-created_at')
    serializer_class=posts_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class Postsdetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Posts.objects.all()
    serializer_class=posts_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]

class commentlistview(generics.ListCreateAPIView):
    queryset=Comments.objects.all()
    serializer_class=comments_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class likelistview(generics.ListCreateAPIView):
    queryset=Likes.objects.all()
    serializer_class=likes_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class followlistview(generics.ListCreateAPIView):
    queryset=Follow.objects.all()
    serializer_class=follow_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)
