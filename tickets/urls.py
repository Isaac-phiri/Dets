from django.urls import path
from .views import *

urlpatterns = [
    path('tickets/', tickets, name='tickets')
]
