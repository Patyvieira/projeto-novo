from django.urls import path
from .views import *

urlpatterns = [
    path('', index_listar, name='index_listar'),
]