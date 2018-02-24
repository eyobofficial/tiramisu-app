from django.contrib import admin

# Import Models
from .models import Catagory, Brand, Tag, Product, Inventory


# Register Catagory, Brand & Tag Models
admin.site.register(Catagory)
admin.site.register(Brand)
admin.site.register(Tag)


# Register Product Model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'catagory',
        'brand',
        'price',
        'on_sale',
        'created_at',
        'updated_at'
    )
    list_filter = (
        'brand',
        'catagory',
        'on_sale',
    )


# Register Inventory Model
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'stock',
    )
