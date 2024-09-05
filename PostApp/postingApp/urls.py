from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_display, name='home'),
    path('makepost/', views.make_a_post, name='post'),
    path('editpost/<int:pk>/', views.edit_post, name='edit_post'),
]
