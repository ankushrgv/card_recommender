from django.conf.urls import url

import views

urlpatterns = [
	url(r'^$',views.Index.as_view(), name='index'),
	url(r'^cards$',views.CardList.as_view(), name='cardlist'),
	url(r'^cards/(?P<pk>[\d]+)/$',views.CardDetails.as_view(), name='carddetails'),
]