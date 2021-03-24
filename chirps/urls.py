from django.contrib import admin
from django.urls import path
from .views import *

app_name = "chirps"

urlpatterns = [
    path('', chirps_list_view),
    path('chirp-detail/<int:chirp_id>', chirp_detail_view),
    path('chirp-create', chirp_create_view),
    path('chirp-delete/<int:chirp_id>', chirp_delete_view),
    path('chirp-action', chirp_action_view),
]
