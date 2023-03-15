from django.urls import path

from .views import create_box, box_confirm

urlpatterns = [
    path('check/', create_box, name='check'),
    path('codebox/', box_confirm, name='codebox'),
    path('open_boxes/', box_confirm, name='open_boxes')
]
