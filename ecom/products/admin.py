from django.contrib import admin
from .models import Product

class showProduct(admin.ModelAdmin):
    list_display= ["title", "desc", "pub_date","product_img"]
            
admin.site.register(Product, showProduct)