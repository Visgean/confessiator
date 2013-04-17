from django.core.management.base import BaseCommand, CommandError
from secrets.models import Confession


class Command(BaseCommand):
	help = 'Tries to post all the approved confessions'

	def handle(self, *args, **options):
		for c in Confession.objects.filter(approved=True, posted = False)[:5]:
			api = c.wall.get_graph_api()
			message = api.put_object(c.wall.facebook_id, "feed", message=c.content.encode('utf-8'))
			c.posted = True
			c.save()