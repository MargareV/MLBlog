from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from . models import Post

class LatestPostsFeed(Feed):
	title = 'My Blog'
	link = '/blog/'
	description = 'New Posts Of My Blog.'

	def items(self):
		return Post.published.all()[:4]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return truncatewords(item.body, 30)
