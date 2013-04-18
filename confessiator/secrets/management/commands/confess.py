from django.core.management.base import BaseCommand, CommandError
from secrets.models import Confession
from facebook import GraphAPIError
from ssl import SSLError

class Command(BaseCommand):
	help = 'Tries to post all the approved confessions'

	def handle(self, *args, **options):
		for c in Confession.objects.filter(approved=True, posted = False)[:3]:
			api = c.wall.get_graph_api()

			fql = u"""SELECT message FROM stream WHERE source_id={0} AND message='{1}' """.format(c.wall.facebook_id, c.content)
			try:
				posted = c.wall.owner.graph_api.fql(fql.encode('utf-8')) # we have to use users api as wall api cannot do fql
				if posted: 
					c.posted = True
					c.save()
					continue # lets not do anuthing with that
			except:
				pass

			try:
				message = api.put_object(c.wall.facebook_id, "feed", message=c.content.encode('utf-8'))
				c.posted = True
			except GraphAPIError, e:
				if e == '(#506) Duplicate status message':
					c.posted = True
			except SSLError:
				c.posted = True

			c.save()