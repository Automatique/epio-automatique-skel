from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.home', name='home'),
    url(r'^chummee/', include('foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^postmark/", include("postmark.urls")),
)