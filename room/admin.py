from django.contrib import admin
from .models import Category, Room

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('title',)}