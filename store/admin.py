from django.contrib import admin
from .models import *

class ClientUserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'is_active', 'is_staff', 'is_superuser')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'joined_date', 'category_image',)
    prepopulated_fields = {'slug': ('category_name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_category', 'joined_date', 'product_adder', 'product_image',)
    prepopulated_fields = {'product_slug': ('product_name',)}

admin.site.register(Client, ClientUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Banner)
