from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('product.views',
    # Examples:
    url(r'^store/$', 'product', name="product"),
    url(r'^store/shipping/', 'shipping', name="productshippingoption"),
    # url(r'^$', 'product_checkout.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
