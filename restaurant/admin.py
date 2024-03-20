from django.contrib import admin

from .models import Category, Restaurant, FoodType

class CategoryAdmin(admin.ModelAdmin):
    ...
class FoodTypeAdmin(admin.ModelAdmin):
    ...

class RestaurantAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(FoodType, FoodTypeAdmin)

