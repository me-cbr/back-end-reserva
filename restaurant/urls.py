from django.urls import path

from . import views

app_name = 'restaurants'

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurants/category_id/<int:category_id>/', views.category, name='category_id'),
    path('recipes/search/', views.search, name="search"),
]
