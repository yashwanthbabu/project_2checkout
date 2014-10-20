from django.shortcuts import render, render_to_response, \
    HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

from .models import Product, ProductShippingOption
from .forms import ProductForm, ProductShippingOptionForm

def product(request):
	form = ProductForm()
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return HttpResponseRedirect(reverse('productshippingoption'))
	return render_to_response("product.html",{'form': form}, context_instance=RequestContext(request))


def shipping(request):
	form = ProductShippingOptionForm()
	if request.method == "POST":
		form = ProductShippingOptionForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('product'))
	return render_to_response("shipping.html", {'form': form}, context_instance=RequestContext(request))