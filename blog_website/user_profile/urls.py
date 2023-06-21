from django.urls import path

from user_profile.views import login_user

from .views import *

# 'login/' url is reserved in codeanywhere; therefore changed to 'blog_login/'
urlpatterns = [
    path('blog_login/', login_user, name='login'),
    path('register_user/', register_user, name='register_user'),
]
