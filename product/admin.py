from django.contrib import admin

from .models import Product, ProductShippingOption

class ProductAdmin(admin.ModelAdmin):
	search_fields = ["merchant"]
	display_fields = ["merchant", "created"]

class ProductShippingOptionAdmin(admin.ModelAdmin):
	display_fields = ["full_name", "created"]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductShippingOption, ProductShippingOptionAdmin)