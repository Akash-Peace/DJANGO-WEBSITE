"""sign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from signin import views

handler500 = views.handler500 #in some code: handler500 = myapp.views.handler500 #here maybe myapp = signin , i think so.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin', views.si, name = 'signup'),
    path('', views.sav, name = 'loginpage'),
    path('main/', views.imp, name = 'mainpage'),
    path('file/', views.file, name='mainfile'),
    path('file-edit/(p?<temp>\d+)/$', views.edit, name='mainfileedit'),
    path(r'score/(p?<temp>\d+)/$', views.score, name = 'score'),
]

