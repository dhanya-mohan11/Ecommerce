from django.contrib import admin
from .models import Category,Product

# Register your models here.

# admin.site.register(Category)
# admin.site.register(Product)


class CategoryAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug':('name',)}

admin.site.register(Product, ProductAdmin)