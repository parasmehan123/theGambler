"""sample URL Configuration

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
from users import views as user_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('casino/', include('casino.urls')),
    path('register/',user_views.register, name='register'),
    path('profile/',user_views.profile, name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='casino/index.html'),name='logout'),
    #Edit user_view.profile to user_view.queryi here and create functions in user/views.py
    path('profile/query1',user_views.profile, name='query1'),
    path('profile/query2',user_views.profile, name='query2'),
    path('profile/query3',user_views.profile, name='query3'),
    path('profile/query4',user_views.profile, name='query4'),
    path('profile/query5',user_views.profile, name='query5'),
    path('profile/query6',user_views.profile, name='query6'),
    path('profile/query7',user_views.profile, name='query7'),
    path('profile/query8',user_views.profile, name='query8'),
    path('profile/query9',user_views.profile, name='query9'),
    path('profile/query10',user_views.profile, name='query10'),
    path('profile/query11',user_views.profile, name='query11'),
    path('profile/query12',user_views.profile, name='query12'),
    path('profile/query13',user_views.profile, name='query13'),
    path('profile/query14',user_views.profile, name='query14'),
    path('profile/query15',user_views.profile, name='query15'),
    path('profile/query16',user_views.profile, name='query16'),
    path('profile/query17',user_views.profile, name='query17'),


]
