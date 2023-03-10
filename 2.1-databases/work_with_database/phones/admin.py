from django.contrib import admin
from .models import Phone

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    # 'name', 'price', 'image', 'release_date', 'lte_exists', 'slug'
    list_display = ['id', 'name', 'price', 'image', 'release_date', 'lte_exists', 'slug']
    list_filter = ['name', 'price', 'release_date', 'lte_exists', 'slug']

