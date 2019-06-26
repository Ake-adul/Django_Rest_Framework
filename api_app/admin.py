from django.contrib import admin
from .models import Product, Category

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [p.name for p in Product._meta.fields]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [c.name for c in Category._meta.fields]