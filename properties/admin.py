from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['location', 'category', 'cost']

 
admin.site.register(Location)
admin.site.register(FAQ)
admin.site.register(Category)