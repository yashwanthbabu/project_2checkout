from django.shortcuts import render, render_to_response, \
    HttpResponseRedirect, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
	import ipdb;ipdb.set_trace()
	print request.user
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


def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            else:
                state = "Your account is not active, Contact Admin."
        else:
            messages.success(request, "Your Username/Password were incorrect")
            return render(request, "registration/login.html")

    return redirect(reverse('product'), args={'state': state,
                                           'username': username,
                                           'password': password})


def logout(request):
    """Logs out user"""
    auth_logout(request)
    messages.success(request, "You Have Successfully Logged Out")
    return redirect(reverse("product"), args=[])