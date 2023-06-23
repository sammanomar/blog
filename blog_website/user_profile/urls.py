from django.urls import path

from user_profile.views import login_user

from .views import *

# 'login/' 'logout/' url are reserved in codeanywhere; therefore changed to 'blog_login/' 'blog_logout/'
urlpatterns = [
    path('blog_login/', login_user, name='login'),
    path('blog_logout/', logout_user, name='logout'),
    path('register_user/', register_user, name='register_user'),
    path('profile/', profile, name='profile'),
    path('change_profile_picture/', change_profile_picture,
         name='change_profile_picture'),
    path('my_blogs/', my_blogs, name='my_blogs'),
]
