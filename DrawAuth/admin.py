from django.contrib import admin
from .models import DrawAuth_Users, DrawAuth_Icons, DrawAuth_TestImages

# Register your models here.


admin.site.register(DrawAuth_Icons)
admin.site.register(DrawAuth_Users)
admin.site.register(DrawAuth_TestImages)
