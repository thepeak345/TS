from django.urls import path

from .views import create_box, box_confirm, get_all_games, exit_box, enter_box, box_info, preferences_box, another_box

urlpatterns = [
    path('check/', create_box, name='check'),
    path('codebox/', box_confirm, name='codebox'),
    path('open_boxes/', get_all_games, name='open_boxes'),
    path('open_boxes/<int:pk>/', box_info, name='box_info'),
    path('enter_box/<int:pk>/', enter_box, name='enter_box'),
    path('leave_box/', exit_box, name='exit_box'),
    path('start_game/', preferences_box, name='start_game'),
    path('another_box/', another_box, name='another_box'),  # todo change url
]
