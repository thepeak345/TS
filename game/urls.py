from django.urls import path

from .views import create_box, box_confirm, opened

urlpatterns = [
    path('check/', create_box, name='check'),
    path('codebox/', box_confirm, name='codebox'),
    path('opened/', opened, name='opened'),
    # path('box/<int:pk>/', None)
]
