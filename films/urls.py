from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('film/<int:film_id>/', views.detail, name='detail'),
]