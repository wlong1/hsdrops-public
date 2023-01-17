from app.models import Feature
from app.update import linkgrabber
from datetime import datetime as dt
import pytz


def check_drops():
    # Make placeholder time, PST since it's Blizzard's timezone
    before = dt(2077, 1, 1, 0, tzinfo=pytz.timezone('US/Pacific'))
    after = dt(2077, 12, 1, 0, tzinfo=pytz.timezone('US/Pacific'))

    latest = Feature.objects.latest('publish_date')
    recent = linkgrabber.grab_links()
    for article in recent:
        data = linkgrabber.search_info(article)
        if (data['active']) and (data['title'] != latest.title):
            Feature.objects.create(
                title = data['title'],
                link = data['link'],
                publish_date = dt.now(tz=pytz.timezone('US/Pacific')), 
                start_date = before,
                end_date = after,
                )

