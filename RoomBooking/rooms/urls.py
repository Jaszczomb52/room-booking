from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('room/<str:pk>', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('buildings', views.buildings, name='buildings'),
    path('building/<str:pk>/', views.building, name="building"),
    path('create-building/', views.createBuilding, name='create-building'),
    path('update-building/<str:pk>/', views.updateBuilding, name="update-building"),
    path('delete-building/<str:pk>/', views.deleteBuilding, name="delete-building"),
    path('create-user/', views.createUser, name="create-user"),
    path('users',views.users, name="users"),
    path('create-reservations/', views.createReservation, name="create-reservations"),
    path('reservations', views.reservations, name="reservations"),
]

