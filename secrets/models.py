import facebook

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from social_auth.models import UserSocialAuth


from trendyou.fbook.tools import GraphAPI 

class UserProfile(models.Model):
    user = models.ForeignKey(User)

	def __unicode__(self):
		return self.user.username

	@property
	def facebook_profile(self):
		#return UserSocialAuth.objects.filter(user=self.user, provider="facebook")[0]
		return self.user.social_auth.all()[0] if len(self.user.social_auth.all()) else None

	@property
	def graph_api_key(self):
		return self.facebook_profile.tokens["access_token"]

	@property
	def graph_api(self):
		return facebook.GraphAPI(self.graph_api_key, timeout=1)






class Secret(models.Model):
    content = models.TextField(_('Your secret'))
    
    approved = models.BooleanField(_('Was this approved by moderators?'), default=False)
    posted = models.BooleanField(_('Was it posted to page/group?'), default=False)

    class Meta:
        verbose_name = _('Secret')
        verbose_name_plural = _('Secrets')

    def __unicode__(self):
        return self.content


class Organization(models.Model):
	name = models.CharField(max_length=20)




    class Meta:
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')

    def __unicode__(self):
        return self.name
