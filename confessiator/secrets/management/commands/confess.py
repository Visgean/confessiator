from django.core.management.base import BaseCommand, CommandError
from secrets.models import Confession


class Command(BaseCommand):
	help = 'Tries to post all the approved confessions'

	def handle(self, *args, **options):
		for c in Confession.objects.filter(approved=True, posted = False):
			api = c.wall.get_graph_api()
			message = api.put_object(c.wall.facebook_id, "feed", message=u"'{0}'".format(c.content))
			c.posted = True
			c.save()

			self.stdout.write('{0} was synced. \n'.format(c.content))