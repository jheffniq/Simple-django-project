from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name = "loginUser"),
    path('logout/', views.logoutUser, name = "logoutUser"),
    path('register/', views.registerUser, name = "registerUser"),


    path('',views.home, name = "home"),
    path ('post/<str:pk>/', views.room, name = "room"),
    path ('profile/<str:pk>',views.userProfile, name = "User Profile"),
    path ('create-post/',views.CreateRoom, name="Create Room"),
    path ('update/<str:pk>/',views.updateRoom, name="Update Room"),
    path ('delete-post/<str:pk>/',views.deleteRoom, name="Delete Room"),

    path ('delete-message/<str:pk>/',views.deleteMessage, name="Delete Message"),
    ]