from django.contrib import admin

# Import Models
from .models import (
    Catagory,
    Brand,
    Tag,
    Unit,
    Product,
    Section,
    Inventory,
)

# Customize Admin Site Header & Title
admin.site.site_header = 'Tiramisu Supermarket Catalog'
admin.site.site_title = 'Tiramisu Supermarket Catalog'


# Register Catagory, Brand, Tag & Unit Models
admin.site.register(Catagory)
admin.site.register(Tag)
admin.site.register(Unit)


# Register Brand Model
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', )
    list_filter = ('featured', )

# Register Product Model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'catagory',
        'brand',
        'unit',
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
