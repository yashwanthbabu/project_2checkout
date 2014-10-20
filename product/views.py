from django.shortcuts import render, render_to_response, \
    HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

from .models import Product, ProductShippingOption, CreditCardDetails
from .forms import ProductForm, ProductShippingOptionForm, CreditCardDetailsForm

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
			return HttpResponseRedirect(reverse('creditcarddetails'))
	return render_to_response("shipping.html", {'form': form}, context_instance=RequestContext(request))


def creditcarddetails(request):
	form = CreditCardDetailsForm()
	if request.method == "POST":
		form = CreditCardDetailsForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('success'))
	return render_to_response("Credit_Card_Details.html", {'form': form}, context_instance=RequestContext(request))