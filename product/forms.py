from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from .models import Product, ProductShippingOption, CreditCardDetails

class ProductForm(ModelForm):
	class Meta:
		model = Product
		exclude = ('merchant', )


class ProductShippingOptionForm(ModelForm):
	class Meta:
		model = ProductShippingOption
		exclude = ('merchant', 'product', )


class CreditCardDetailsForm(ModelForm):
	class Meta:
		model = CreditCardDetails
		exclude = ('merchant', )
