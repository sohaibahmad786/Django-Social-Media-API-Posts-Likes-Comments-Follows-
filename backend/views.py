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
from .models import Student
from .serializer import Student_serilizer
from django.conf import settings
from rest_framework.filters import SearchFilter
from datetime import datetime, timedelta
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Register
from .serializer import Register_serilizer
from .models import Note
from .serializer import Note_serilizer
from .models import Category,Products
from .serializer import category_serilizer,products_serilizer
from .models import Post,Comment
from .serializer import Comment_serilizer,Post_serilizer

from .models import Posts,Comments,Likes,Follow
from .serializer import comments_serilizer,posts_serilizer,likes_serilizer,follow_serilizer


  
# ______________________ Student Managment API___________________
class student_list(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serilizer
class student_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serilizer
    

# _____________________ Banking Account API __________
# class account_list(generics.ListCreateAPIView):
#     queryset=Account.objects.all()
#     serializer_class=Account_serilizer
#     authentication_classes=[JWTAuthentication]
#     permission_classes=[permissions.AllowAny]

# class account_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Account.objects.all()
#     serializer_class=Account_serilizer
#     authentication_classes=[JWTAuthentication]
#     permission_classes=[permissions.AllowAny]


# ___________________ register________

class Register_list(ListCreateAPIView):
    queryset=Register.objects.all()
    serializer_class=Register_serilizer
    permission_classes=[permissions.AllowAny]


class Note_list(generics.ListCreateAPIView):

    queryset=Note.objects.all()
    serializer_class=Note_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
   
class Note_detail(generics.RetrieveUpdateDestroyAPIView):

    queryset=Note.objects.all()
    serializer_class=Note_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]


# _______________ Products API view _________________
class Productlistview(generics.ListCreateAPIView):
    queryset=Products.objects.all()
    serializer_class=products_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['category']
    search_fields=['name']
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Products.objects.all()
    serializer_class=products_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]

# _______________________ Blog APi_______________________
class postlist(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=Post_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
class postdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=Post_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]
class comment_view(generics.CreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=Comment_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

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