from django.contrib import admin

# Import Models
from .models import (
    Catagory,
    Brand,
    Tag,
    Product,
    Section,
    Inventory,
)


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
    list_filter = ('brand', 'catagory', 'on_sale', )


# Register Section Model
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'floor', )
    list_filter = ('floor', )


# Register Inventory Model
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'stock', 'section', )
    list_filter = ('section', )
