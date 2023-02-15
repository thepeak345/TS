from django.urls import path
from .views import (
    login_view,
    logout_view,
    signup,
    user_confirm
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
    path('otp/', user_confirm, name='otp'),
    path('password-change/', 'django.contrib.auth.views.password_change', name='password_change'),
    path('password-change/done/', 'django.contrib.auth.views.password_change_done', name='password_change_done'),


]
