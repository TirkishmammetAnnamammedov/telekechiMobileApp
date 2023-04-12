from django.contrib import admin
from .models import *

class ClientUserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'is_active', 'is_staff', 'is_superuser')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'joined_date', 'category_image',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_category', 'joined_date', 'product_adder', 'product_image',)

admin.site.register(Client, ClientUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Dukan)
admin.site.register(Banner)
