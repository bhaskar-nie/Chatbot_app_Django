from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('getResponse', getResponse, name="getResponse"),
]