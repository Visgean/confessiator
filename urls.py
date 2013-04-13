from django.contrib.auth.views import login, logout_then_login
from django.conf.urls import patterns, include, url

from confessiator.settings.base import MEDIA_ROOT, MEDIA_URL

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
   	url(r'^logout/$', logout_then_login, name="logout"),
	url(r'', include('social_auth.urls')),
	)


urlpatterns += patterns('confessiator.secrets.views',
	url(r'^$', view='home', name='home'),
	url(r'^select_wall/$', view='select_wall', name='select_wall'),
	url(r'^import_page/(?P<uid>\d+)/$', view='import_page', name='import_page'),
	
	url(r'^p/(?P<slug>[-\w]+)/detail/$', view='wall_detail', name='wall_detail'),
	url(r'^p/(?P<slug>[-\w]+)/$', view='post', name='post'),
	# url(r'^/p/(?P<slug>\w+)/moderate$', view='moderate', name='moderate'),
	# url(r'^/p/(?P<slug>\w+)/associate_admin$', view='moderate', name='moderate'),
	)

urlpatterns += patterns('',
	(r'^%s(?P<path>.*)$' % MEDIA_URL[1:], 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
	)
