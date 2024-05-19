from django.urls import path, include
from .views import *



urlpatterns = [
    
        path('register/',  create_user, name='register')
]
