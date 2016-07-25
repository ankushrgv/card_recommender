"""
card_recommender URL Configuration

"""

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^', include('apps.cards.urls', namespace='cards')),
	url(r'^admin/', admin.site.urls),
]
