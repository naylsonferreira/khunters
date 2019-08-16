from django.urls import path
from .views import *

urlpatterns = [
    path('', main_job, name="Main"),
]
