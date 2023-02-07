from django.urls import path

from auth_2023.web.views import index, create_user_and_login, show_profile, ProfileView

urlpatterns = (
    path('', index, name='index'),
    path('login/', create_user_and_login),
    path('profile/1/', show_profile, name='show profile'),
    path('profile/2/', ProfileView.as_view(), name='show profile'),
)