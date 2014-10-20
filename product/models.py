from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	merchant = models.ForeignKey(User)
	PYTHON = "python"
	DJANGO = "django"
	BOOTSTRAP = "bootstrap"
	product_choices = (
		(PYTHON, 'python'),
		(DJANGO, 'django'),
		(BOOTSTRAP,'bootstrap'),
			)
	product = models.CharField(max_length=10, choices=product_choices, default=DJANGO)
	price = models.IntegerField(max_length=10, null=False, blank=False)
	quantity = models.IntegerField(max_length=10, null=False, blank=False)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.merchant
		return unicode(self.created)


class ProductShippingOption(models.Model):
	merchant = models.ForeignKey(User)
	INDIA = "IND"
	AMERCIA = "US"
	NEWZEALAND = "NWZ"
	country_choices = (
		(INDIA, "IND"),
		(AMERCIA,"US"),
		(NEWZEALAND," NWZ"),
			)
	country = models.CharField(max_length=10, choices=country_choices, default=INDIA)
	full_name = models.CharField(max_length=75, null=False, blank=False, default='')
	address1 = models.CharField(max_length=100, null=False, blank=False)
	address2 = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=20, null=False, blank=False)
	postal_code = models.CharField(max_length=6, null=False, blank=False)
	state = models.CharField(max_length=20, null=False, blank=False)
	phone = models.IntegerField(max_length=35, null=False, blank=False)
	email = models.EmailField(max_length=20, null=False, blank=False)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.full_name
		return unicode("%s: %s" % (self.email))

