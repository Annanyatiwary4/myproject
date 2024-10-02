from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateRoomView, name='home'),  # Use CreateRoomView for home if it handles room creation
    path('create-room/', views.CreateRoomView, name='create_room'),
    path('join-room/', views.JoinRoomView, name='join_room'),
    path('room/<str:room_id>/<str:username>/', views.RoomView, name='room'),
]
