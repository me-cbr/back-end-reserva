from django.urls import path

from . import views

app_name = 'restaurants'

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurants/category_id/<int:category_id>/', views.category, name='category_id'),
    path('restaurants/<int:id>/', views.restaurant, name='restaurant'),
    path('restaurants/<int:id>/classification/', views.classification, name='classification'),
    path('restaurants/<int:id>/classification/post/', views.restaurant_classification, name='post'),
]
