from django.core.management.base import BaseCommand, CommandError
from secrets.models import Confession
from facebook import GraphAPIError
from ssl import SSLError

class Command(BaseCommand):
	help = 'Tries to post all the approved confessions'

	def handle(self, *args, **options):
		for c in Confession.objects.filter(approved=True, posted = True):
			api = c.wall.get_graph_api()

			fql = u"""SELECT message FROM stream WHERE source_id={0} AND message='{1}' """.format(c.wall.facebook_id, c.content)
			try:
				posted = c.wall.owner.graph_api.fql(fql.encode('utf-8')) # we have to use users api as wall api cannot do fql
				print posted
			except:
				print post
