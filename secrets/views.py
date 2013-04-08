from django.utils.translation import ugettext as _
from django.views.generic import TemplateView, DetailView
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404


home = TemplateView.as_view(template_name="home.html")
