from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Register
from .models import Posts
from .models import Comments
from .models import Likes
from .models import Follow

admin.site.register(Follow)
admin.site.register(Likes)
admin.site.register(Comments)
admin.site.register(Posts)
admin.site.register(Register,UserAdmin)
# Register your models here.
