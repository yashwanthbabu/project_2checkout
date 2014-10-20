from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from .models import Product, ProductShippingOption

class ProductForm(ModelForm):
	class Meta:
		model = Product


class ProductShippingOptionForm(ModelForm):
	class Meta:
		model = ProductShippingOption
