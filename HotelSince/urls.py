"""RoyalCity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth.decorators import login_required 

from django.contrib.auth.views import LoginView, logout_then_login
from SinceApp.hotel.views import  home, error404,error500

from django.conf.urls import handler404, handler500
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotel/',include(('SinceApp.hotel.urls','hotel'))),
    path('',login_required(home) ,name = "index" ),

    path('accounts/login/',LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/',logout_then_login, name="logout"),

]
handler404 = error404.as_view()
handler500 = error500.as_error_view()