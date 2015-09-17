from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^ideas/', include('ideas.urls')),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'joins.views.home', name='home'),
    # url(r'^testhome$', 'mwday.views.testhome', name='testhome'),
    url(r'^(?P<ref_id>.*)$', 'joins.views.share', name='share'),
    # url(r'^home2/$', 'mwday.views.home2', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^ideas/', include('ideas.urls')),
)
