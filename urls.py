from django.conf.urls import patterns, include, url

from secretpost.settings.base import MEDIA_ROOT, MEDIA_URL

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'', include('social_auth.urls')),
	)


urlpatterns += patterns('secretpost.secrets.views',
	url(r'^$', view='home', name='home'),
	url(r'^select_page$', view='select_page', name='select_page'),
	# url(r'^/p/(?P<slug>\w+)/$', view='post', name='post'),
	# url(r'^/p/(?P<slug>\w+)/moderate$', view='moderate', name='moderate'),
	# url(r'^/p/(?P<slug>\w+)/associate_admin$', view='moderate', name='moderate'),
	)

urlpatterns += patterns('',
	(r'^%s(?P<path>.*)$' % MEDIA_URL[1:], 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
	)
