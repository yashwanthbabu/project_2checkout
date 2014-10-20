from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('product.views',
    # Examples:
    url(r'^product/$', 'product', name="product"),
    url(r'^product/shipping/', 'shipping', name="productshippingoption"),
    url(r'^product/payment/', 'creditcarddetails', name="creditcarddetails"),
    url(r'^product/paymentsuccess/', TemplateView.as_view(template_name="payment_success.html"), name="success"),
    # url(r'^$', 'product_checkout.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
