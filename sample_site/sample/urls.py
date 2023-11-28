from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = "home"),
    path('home/details/<int:id>', views.details, name = "details"),
    path('eng/worksheet-1', views.worksheet1, name = "worksheet1")
]