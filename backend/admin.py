from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Student
from .models import Register
from .models import Note
from .models import Category
from .models import Products
from .models import Post
from .models import Comment
from .models import Posts
from .models import Comments
from .models import Likes
from .models import Follow

admin.site.register(Follow)
admin.site.register(Likes)
admin.site.register(Comments)
admin.site.register(Posts)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Note)
admin.site.register(Register,UserAdmin)
admin.site.register(Student)
# Register your models here.
