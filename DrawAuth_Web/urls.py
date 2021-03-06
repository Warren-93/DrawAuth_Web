"""Django_GraphicalPasswords URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from DrawAuth.views import login_programmatically, Login, Signup

from pages.views import (
    home_view,
    graphical_login_view,
    hash_test,
    reg_hash,
    username_select_view,
    selected_user_image_view,
    get_user_image,
    testcall,
    startlogin,
    reguser,
    selected_user_image_reg_view,
)

urlpatterns = [


    path('', home_view, name='home'),
    path('graphical_login/', graphical_login_view, name='graphical_login'),
    path('admin/', admin.site.urls),
    path('hash/', hash_test, name='hash'),
    path('reg_hash/', reg_hash, name='reg_hash'),
    path('get_user_image', get_user_image, name='get_user_image'),

    path('username/startlogin/', startlogin, name="startlogin"),
    path('reguser/testcall/', testcall, name="testcall"),
    path('reguser/', reguser, name='reguser'),
    path('loginprog/', login_programmatically, name='login_prog'),
    path('username/', username_select_view, name='username_select'),
    path('selected_user/', selected_user_image_view, name='selected_user_image'),
    path('selected_user_reg/', selected_user_image_reg_view, name='selected_user_image_reg'),

    path('DrawAuth/', include('django.contrib.auth.urls')),
    path('DrawAuth/', include('DrawAuth.urls')),
    path('DrawAuth/login/', Login, name='Login'),
    path('DrawAuth/signup/', Signup, name='Signup')

]

urlpatterns += staticfiles_urlpatterns()