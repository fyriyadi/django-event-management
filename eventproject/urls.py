"""eventproject URL Configuration

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
from django.urls import path, include
from django.views.generic.base import TemplateView
from account_app import views as account_app_views
from event_app import views as event_app_views

urlpatterns = [
   
    path('', account_app_views.homePage, name='home'),
    path('admin/', admin.site.urls),
    path('register/',account_app_views.registerPage, name="register"),
    path('login/',account_app_views.loginPage, name="login"),
    path('logout/', account_app_views.logoutUser, name="logout"),
    path('event/home/', event_app_views.eventPage),
    path('event/<int:id>', event_app_views.eventDetail, name='eventdetail'),
    path('event/register/<int:id>', event_app_views.eventRegister, name='eventregister'),

    path('accounts/', include('account_app.urls')),
    # default django user auth url
    # path('accounts/', include('django.contrib.auth.urls')),
]
