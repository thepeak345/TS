from django.urls import path

from .views import create_box, box_confirm, get_all_games, close_box

urlpatterns = [
    path('check/', create_box, name='check'),
    path('codebox/', box_confirm, name='codebox'),
    path('open_boxes/', get_all_games, name='open_boxes'),
    path('open_boxes/<int:pk>/', get_all_games, name='open_boxes'),
    path('close_box/', close_box, name='close_box'),
    path('close_box/<int:pk>/', close_box, name='close_box')

]
