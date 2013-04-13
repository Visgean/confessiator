import random
import string

from django.utils.translation import ugettext as _
from django.views.generic import TemplateView, DetailView
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from secrets.models import UserProfile, WallObject
from secrets.forms import WallForm, ConfessionForm

get_pages = lambda u: [u.graph_api.get_object(p['page_id']) for p in u.graph_api.fql('SELECT page_id FROM page_admin WHERE uid={0}'.format(u.get_fuid()))]
random_token = lambda l: "".join( [random.choice(string.letters) for i in xrange(l)] )


def home(request):
    if request.user.is_authenticated():
        p, c = UserProfile.objects.get_or_create(user=request.user)  # users must have profiles!
        return direct_to_template(request, 'home.html', {
            'walls': p.owned_walls.all()
        })
    else:
        return direct_to_template(request, 'intro.html', {})


@login_required
def select_wall(request):
    pages = get_pages(request.user.get_profile())

    return direct_to_template(request, 'select_page.html', {
        'pages': pages
    })


@login_required
def import_page(request, uid):
    p = request.user.get_profile()
    r = p.graph_api.fql('SELECT name, username, access_token, page_id, page_url, description FROM page WHERE page_id={0}'.format(uid))
    page = r[0] if r else None
    
    if not page:
        HttpResponseRedirect('/')

    if request.POST:
        form = WallForm(request.POST)

        if form.is_valid():
            wall = form.save(commit=False)
            
            wall.owner = request.user.get_profile()
            wall.secret_token = page['access_token']
            wall.facebook_id = page['page_id']
            wall.wall_type = 'p'
            wall.url = page['page_url']
            wall.admin_token = random_token(27)

            wall.save()

            return HttpResponseRedirect(wall.get_absolute_url())
    else:
        form = WallForm(initial={
            'name' : page['name'],
            'content' : page['description'],
            'slug' : page['username'].lower(),
            })

    return direct_to_template(request, 'import_page.html', {
        'form': form,
    })


@login_required
def wall_detail(request, slug):
    wall = get_object_or_404(WallObject, slug = slug, owner = request.user.get_profile())

    return direct_to_template(request, 'wall_detail.html', {
        'wall' : wall
        })



def post(request, slug):
    wall = get_object_or_404(WallObject, slug = slug)
    if request.POST:
        form = ConfessionForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.wall=wall
            post.save()

            HttpResponseRedirect('.')
    else:
        form = ConfessionForm()

    return direct_to_template(request, 'post.html',{
        'wall' : wall,
        'form' : form,
        })
