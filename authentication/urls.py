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
    path('otp/', user_confirm, name='otp')


]
