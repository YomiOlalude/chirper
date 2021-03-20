from django.contrib import admin
from django.urls import path
from .views import *

app_name = "chirps"

urlpatterns = [
    path('', chirps_list_view),
    path('create-chirp', chirp_create_view),
]
