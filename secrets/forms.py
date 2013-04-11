from django.forms import ModelForm

from secrets.models import WallObject




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
