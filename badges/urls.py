from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import badger
badger.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'badges.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'badges.views.home'),
	url('', include('social.apps.django_app.urls', namespace='social')),
	url(r'^login/$', 'badges.views.home'),
	url(r'^logout/$', 'badges.views.logout'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^badges/', include('badger.urls')),
)
