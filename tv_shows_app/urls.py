from django.urls import path
from . import views

urlpatterns = [
    path('', views.allshows),
    path('/<int:id>/', views.oneshow),
    path('/<int:id>/edit/', views.edit),
    path('/new/', views.new),
    path('/create/', views.create),
    path('/<int:id>/delete/', views.delete),
    path('/<int:id>/update/', views.update),
]