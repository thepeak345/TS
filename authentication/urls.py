from django.urls import path
from .views import (
    login_view,
    logout_view,
    signup,
    user_confirm
)
from . import views

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
    path('otp/', user_confirm, name='otp'),
    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('preferences-reset/', views.preferences_reset, name='preferences_reset')
]
