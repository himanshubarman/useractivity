from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('user/activity/', UserView.as_view(), name='UserView'),
    path('generatedata/', generatedata, name='generatedata'),
]