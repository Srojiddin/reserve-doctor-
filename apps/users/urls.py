from django.urls import path

from apps.users.views import (
    UserCreateView, UserDetailView, UserUpdateView, UserDeleteView, UserProfileView, IndexView
)
from django.contrib.auth import views as auth_views
from . import views
from .views import  logout_view

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('user/detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    # path('register/', views.register, name='register'),
]
