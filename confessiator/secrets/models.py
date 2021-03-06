import facebook

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from social_auth.models import UserSocialAuth

from confessiator.settings.base import FACEBOOK_API_SECRET


# SecretGraphAPI = facebook.GraphAPI(FACEBOOK_API_SECRET)


class UserProfile(models.Model):
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'{0} {1}'.format(self.user.first_name, self.user.last_name)

    @property
    def facebook_profile(self):
        # return UserSocialAuth.objects.filter(user=self.user, provider="facebook")[0]
        return self.user.social_auth.all()[0] if len(self.user.social_auth.all()) else None


    def get_fuid(self):
        'Get Facebook UID'
        return self.facebook_profile.uid


    @property
    def graph_api_key(self):
        return self.facebook_profile.tokens["access_token"]

    @property
    def graph_api(self):
        return facebook.GraphAPI(self.graph_api_key, timeout=1)


class WallObject(models.Model):
    WALL_TYPES = (
        ('g', _('Facebook group')),
        ('p', _('Facebook page')),
    )

    owner = models.ForeignKey(UserProfile, related_name='owned_walls')
    name = models.CharField(_('Name'), max_length=20, unique=True)
    content = models.TextField(_('Content'), help_text=_('Rules for your page, parsed with markdown'), blank=True, null=True)
    secret_token = models.CharField(max_length=140)
    facebook_id = models.CharField(max_length=30, unique=True)
    wall_type = models.CharField(_('Wall type'), max_length=2, choices=WALL_TYPES)
    slug = models.SlugField(_('URL id'), help_text=_('URL identifier for adding new objects'), unique=True)
    
    url = models.URLField(_('URL for wall'), help_text=_('URL adress for the wall'))

    moderated = models.BooleanField(_('Moderated'), help_text=_('Do you want to moderate the posts?'), default=True)

    admin_token = models.CharField(_('Admin password'), blank=True, null=True, max_length=30)
    admins = models.ManyToManyField(UserProfile, blank=True, null=True, )

    @models.permalink
    def get_absolute_url(self):
        return ('wall_detail', (self.slug,))

    @models.permalink
    def get_post_url(self):
        return ('post', (self.slug,))

    @models.permalink
    def get_moderate_url(self):
        return ('moderate', (self.slug,))


    class Meta:
        verbose_name = _('Facebook wall')
        verbose_name_plural = _('Facebook walls')

    def __unicode__(self):
        return self.name

    
    def get_graph_api(self):
        return facebook.GraphAPI(self.secret_token, timeout=1)





class Confession(models.Model):
    content = models.TextField(_('Your secret'))

    approved = models.BooleanField(_('Was this approved by moderators?'), default=False)
    declined = models.BooleanField(_('Was this declined by moderators?'), default=False)
    posted = models.BooleanField(_('Synced to wall?'), default=False)

    last_change = models.DateTimeField(auto_now_add=True)

    wall = models.ForeignKey(WallObject)

    class Meta:
        verbose_name = _('Confession')
        verbose_name_plural = _('Confessions')

    def __unicode__(self):
        return self.content