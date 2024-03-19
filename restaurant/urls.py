from django.urls import path

from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.user, name='user')
]
