from django.utils.translation import ugettext as _
from django.views.generic import TemplateView, DetailView
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from secrets.models import UserProfile, WallObject


get_pages = lambda u: [u.graph_api.get_object(p['page_id']) for p in u.graph_api.fql('SELECT page_id FROM page_admin WHERE uid={0}'.format(uid))]  



def home(request):
	if request.user.is_authenticated():
		p, c = UserProfile.objects.get_or_create(user=request.user) # users must have profiles!
		if c:
			HttpResponseRedirect('/select_page')

		return direct_to_template(request, 'home.html', {})
	else:
		return direct_to_template(request, 'intro.html', {})

def select_page(request):
	pages = get_pages(request.user.get_profile) 


	return direct_to_template(request, 'select_page.html', {
		'pages' : pages
		})