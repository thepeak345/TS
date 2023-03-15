from django.urls import path

from .views import create_box, box_confirm

urlpatterns = [
    path('check/', create_box, name='check'),
    path('codebox/', box_confirm, name='codebox')
]
