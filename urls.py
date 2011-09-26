from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.homepage', name='home'),
    url(r'^foo/', include('foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^postmark/", include("postmark.urls")),
)