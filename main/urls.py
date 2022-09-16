from django.urls import path, reverse
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('post/<str:pk>/', views.post, name='post'),
]
