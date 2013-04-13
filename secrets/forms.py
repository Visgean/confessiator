from django.forms import ModelForm

from secrets.models import WallObject, Confession


class ConfessionForm(ModelForm):
    class Meta:
        model = Confession
        exclude = (
            'approved',
            'declined',
            'posted', 
            'last_change', 
            'wall', 
            )



class WallForm(ModelForm):
    class Meta:
        model = WallObject
        exclude = (
            'owner',
            'secret_token',
            'url', 
            'wall_type', 
            'facebook_id', 
            'slugs',
            'admins', 
            'admin_token'
            )

