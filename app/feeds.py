from django.contrib.syndication.views import Feed
from .models import Feature

 
class rss_feed(Feed):
    title = "Hearthstone Drops"
    link = ""
    description = "RSS feed for HS drops"
 
    def items(self):
        return [Feature.objects.latest('start_date')]

    def item_description(self, item):
        return ""

    def item_title(self, item):
        return "New drops: " +item.title    

    def item_link(self, item):
        return item.link

    def ttl(self):
        return 1440

    def pubdate(self, item):
        return item.publish_date

    def item_updateddate(self, item):
        return item.publish_date
