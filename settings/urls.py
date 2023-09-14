"""
URL configuration for codetrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from settings import views
urlpatterns = [
    path('',views.settings),
    path('leetcode_name/',views.leetcode_name),
    path('leetcode_check/',views.leetcode_check),
    path('codechef_name/',views.codechef_name),
    path('codechef_check/',views.codechef_check),
    path('codeforces_name/',views.codeforces_name),
    path('codeforces_check/',views.codeforces_check),
    path('institute/',views.change_institute),
   
    
    
    
]