from django.contrib import admin
from django.urls import path, include
from .views import recogface

urlpatterns = [
    path('facerecog/',recogface,name='facerecog'),
]
