from django.urls import path
from . import views, feeds

urlpatterns = [
    path('', views.index, name='index'),
    path('history', views.history, name='history'),
    path("rss", feeds.rss_feed(), name ="rss")
]