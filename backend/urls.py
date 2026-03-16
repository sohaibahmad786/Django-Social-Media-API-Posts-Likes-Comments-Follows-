from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import Register_list
from .views import Postslistview,Postsdetailview,commentlistview,likelistview,followlistview


urlpatterns = [
    path('login/',TokenObtainPairView.as_view()),
    path('login/refresh/',TokenRefreshView.as_view()),
    path('register/',Register_list.as_view()),
    path('post/',Postslistview.as_view()),
    path('post/<int:pk>/',Postsdetailview.as_view()),
    path('comment/',commentlistview.as_view()),
    path('like/',likelistview.as_view()),
    path('follow/',followlistview.as_view()),

]
