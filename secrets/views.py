from django.utils.translation import ugettext as _
from django.views.generic import TemplateView, DetailView
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from secrets.models import UserProfile

home = TemplateView.as_view(template_name="home.html")

def home(request):
	if request.user.is_authenticated():
		UserProfile.objects.get_or_create(user=request.user) # users must have profiles!
		return direct_to_template(request, 'home.html', {})
	else:
		return direct_to_template(request, 'intro.html', {})

