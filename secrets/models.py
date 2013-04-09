import facebook

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from social_auth.models import UserSocialAuth


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return '{0} {1}'.format(self.user.first_name, self.user.last_name)

    @property
    def facebook_profile(self):
        # return UserSocialAuth.objects.filter(user=self.user, provider="facebook")[0]
        return self.user.social_auth.all()[0] if len(self.user.social_auth.all()) else None

    @property
    def graph_api_key(self):
        return self.facebook_profile.tokens["access_token"]

    @property
    def graph_api(self):
        return facebook.GraphAPI(self.graph_api_key, timeout=1)




class Organization(models.Model):
    ORG_TYPES = (
            ('g', _('Facebook group')),
            ('p', _('Facebook page')),
        )



    name = models.CharField(max_length=20)
    secret_token = models.CharField(max_length=140)
    facebook_id = models.IntegerField()


    org_type = models.CharField(max_length=2, choices=ORG_TYPES, unique=True)


    slug = models.SlugField(_('URL identifier for your page ?'), unique=True)

    moderated = models.BooleanField(_('Do you want to moderate the posts?'), default=True)
    content = models.TextField(_('Rules for your page, parsed with markdown'))


    password_for_admins = models.CharField(blank=True, null=True, max_length=30)
    admins = models.ManyToManyField(UserProfile)

    url = models.SlugField()

    class Meta:
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')

    def __unicode__(self):
        return self.name


class Secret(models.Model):
    content = models.TextField(_('Your secret'))

    approved = models.BooleanField(_('Was this approved by moderators?'), default=False)
    posted = models.BooleanField(_('Was it posted to page/group?'), default=False)

    org = models.ForeignKey(Organization)

    class Meta:
        verbose_name = _('Secret')
        verbose_name_plural = _('Secrets')

    def __unicode__(self):
        return self.content