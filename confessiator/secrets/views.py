import random
import string
import simplejson

from django.utils.translation import ugettext as _
from django.views.generic import TemplateView, DetailView
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from secrets.models import UserProfile, WallObject, Confession
from secrets.forms import WallForm, ConfessionForm

get_pages = lambda u: [u.graph_api.get_object(p['page_id']) for p in u.graph_api.fql('SELECT page_id FROM page_admin WHERE uid={0}'.format(u.get_fuid()))]
random_token = lambda l: "".join( [random.choice(string.letters) for i in xrange(l)] )

@csrf_exempt
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
    wall = get_object_or_404(WallObject, Q(Q(owner = request.user.get_profile()) | Q(admins = request.user.get_profile())), slug = slug)

    return direct_to_template(request, 'wall_detail.html', {
        'wall' : wall
        })

@login_required
def moderate(request, slug):
    wall = get_object_or_404(WallObject, Q(Q(owner = request.user.get_profile()) | Q(admins = request.user.get_profile())), slug = slug)

    return direct_to_template(request, 'moderate.html', {
        'wall' : wall,
        'posts' : Confession.objects.filter(approved=False, declined=False)
        })



@login_required
def associate_moderators(request, slug, token):
    wall = get_object_or_404(WallObject, slug = slug, admin_token = token)
    wall.admins.add(request.user.get_profile())
    wall.save()

    return HttpResponseRedirect(wall.get_moderate_url())



@login_required
@csrf_exempt
def moderate_post(request, post_id):
    confession = get_object_or_404(Confession, Q(Q(wall_owner = request.user.get_profile()) | Q(wall_admins = request.user.get_profile())), id=post_id)

    if request.POST['type'] == 'accept':
        status_code = 200

        confession.approved = True
        confession.save()

    elif request.POST['type'] == 'decline':
        confession.declined = True
        confession.save()

        status_code = 200

    else:
        status_code = 500


    return HttpResponse(simplejson.dumps({}), content_type="application/json", status=status_code)







def post(request, slug):
    wall = get_object_or_404(WallObject, slug = slug)
    if request.POST:
        form = ConfessionForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.wall=wall
            post.save()

            messages.success(request, _('Your confession is now waiting to be moderated.'))
            HttpResponseRedirect('.')
    else:
        form = ConfessionForm()

    return direct_to_template(request, 'post.html', {
        'wall' : wall,
        'form' : form,
        })


