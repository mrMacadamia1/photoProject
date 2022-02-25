from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('connection/', views.connection, name='connection'),
    path('work/', views.work, name='work'),
]