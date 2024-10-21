from django.urls import path
from . import views

urlpatterns = [
    path('platforms/', views.PlatformList.as_view(), name='platform-list'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('games/', views.GameList.as_view(), name='game-list'),
    path('games/<int:pk>/', views.GameDetail.as_view(), name='game-detail'),
]
