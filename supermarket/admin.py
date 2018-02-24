from django.contrib import admin

# Import Models
from .models import Catagory, Brand, Tag, Product


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
        'on_sale',
        'created_at',
        'updated_at'
    )
