from django.conf.urls.defaults import patterns, include, url
from views import *
# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quefilme.views.home', name='home'),
    # url(r'^quefilme/', include('quefilme.foo.urls')),
    url(r'^$', search_movie, name='search_movie'),
    url(r'^add/$', add_movie),
    url(r'^(?P<slug>\w+)/rate/$', rate_movie),
    url(r'^(?P<slug>\w+)/rate/categories/$', rate_movie_categories),
    url(r'^(?P<slug>\w+)/comment/$', comment_movie, name="comment_movie"),
    url(r'^(?P<slug>\w+)/$', view_movie, name="movie_view"),
   	# Uncomment the admin/doc line below to enable admin documentation:
    
)