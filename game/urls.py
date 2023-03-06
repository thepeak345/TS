from django.urls import path

from .views import create_box

urlpatterns = [
    path('check/', create_box, name='check'),
    path('')
]