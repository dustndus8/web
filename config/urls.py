"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

import accounts.views
import board.views

import reply.views
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('main', board.views.mainPage),
    path('board/create',board.views.create),
    path('board/listGet',board.views.listGet),
    path('board/readGet/<int:bid>',board.views.readGet),
    path('board/deleteGet/<int:bid>',board.views.deleteGet),
    path('board/update/<int:bid>',board.views.update),

    path('reply/create/<int:bid>',reply.views.create),
    path('reply/list',reply.views.list),
    path('reply/read/<int:rid>',reply.views.read),
    path('reply/delete/<int:rid>',reply.views.delete),
    path('reply/update/<int:rid>',reply.views.update),

    #path('user/signup', user.views.singup),
    #path('user/login', user.views.login),
    #?path('user/logout', user.views.logout),
    #path('user/signout/<int:uid>', user.views.signout),

    path('board/like/<int:bid>',board.views.like),
    path('reply/like/<int:rid>',reply.views.like),

    path('accounts/', include('allauth.urls')),

    path('oauth/redirect',accounts.views.getcode),

]
