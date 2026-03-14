from django.urls import path
from .views import student_list,student_detail
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import Register_list
from .views import Note_list,Note_detail
from .views import Productlistview,ProductDetail
from .views import postlist,postdetail,comment_view

from .views import Postslistview,Postsdetailview,commentlistview,likelistview,followlistview


urlpatterns = [
    path('student/',student_list.as_view()),
    path('student/<int:pk>/',student_detail.as_view()),
    path('login/',TokenObtainPairView.as_view()),
    path('login/refresh/',TokenRefreshView.as_view()),
    path('register/',Register_list.as_view()),
    path('note/',Note_list.as_view()),
    path('note/<int:pk>/',Note_detail.as_view()),
    path('product/',Productlistview.as_view()),
    path('product/<int:pk>/',ProductDetail.as_view()),
    # path('post/',postlist.as_view()),
    # path('post/<int:pk>/',postdetail.as_view()),
    # path('comment/',comment_view.as_view()),

    path('post/',Postslistview.as_view()),
    path('post/<int:pk>/',Postsdetailview.as_view()),
    path('comment/',commentlistview.as_view()),
    path('like/',likelistview.as_view()),
    path('follow/',followlistview.as_view()),

]
