from django.contrib import admin

from .models import Product, ProductShippingOption, CreditCardDetails

class ProductAdmin(admin.ModelAdmin):
	search_fields = ["merchant"]
	display_fields = ["merchant", "created"]

class ProductShippingOptionAdmin(admin.ModelAdmin):
	display_fields = ["full_name", "created"]

class CreditCardDetailsAdmin(admin.ModelAdmin):
	display_fields = ["credit_card_number", "created"]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductShippingOption, ProductShippingOptionAdmin)
admin.site.register(CreditCardDetails, CreditCardDetailsAdmin)