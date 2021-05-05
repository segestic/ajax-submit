
from django.urls import path
from .views import *

urlpatterns = [
    path('', index), # index url
    path('ajax-posting/', ajax_posting, name='ajax_posting'),# ajax-posting / name = that we will use in ajax url
]