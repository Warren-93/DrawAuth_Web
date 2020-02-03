from django.contrib import admin
from .models import DrawAuth_user, DrawAuth_testImages, DrawAuth_userIcons
# Register your models here.


admin.site.register(DrawAuth_userIcons)
admin.site.register(DrawAuth_user)
admin.site.register(DrawAuth_testImages)