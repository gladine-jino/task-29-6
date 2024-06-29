from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register,name='register'),
    path('login_view/', views.login_view,name='login_view'),
    path('user_logout/', views.user_logout,name='user_logout'),


]