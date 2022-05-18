from django.contrib import admin

# Register your models here.

from . models import Room, Category, Message


admin.site.register(Room)
admin.site.register(Category)
admin.site.register(Message)
