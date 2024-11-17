from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('change_password/', views.change_password_view, name='change_password'),
    path('users_list/', views.users_list, name='users_list')
]
