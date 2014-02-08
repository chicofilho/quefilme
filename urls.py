from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from facebook_app.views import login
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quefilme.views.home', name='home'),
    # url(r'^quefilme/', include('quefilme.foo.urls')),
    (r'^login$', 'django.contrib.auth.views.login'), 
    (r'^facebook/', include('django_facebook.urls')),
    (r'^accounts/', include('django_facebook.auth_urls')),
    url(r'^movie/', include('movie.urls')),
    #url(r'^login/$', 'facebook_app.views.login'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
