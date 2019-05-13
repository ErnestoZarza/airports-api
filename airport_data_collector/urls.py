from django.conf.urls import url
from .views import ListAirportView, AirportNameListView, AirportIATADetailView, upload_data

urlpatterns = [
    url('airports/list/$', ListAirportView.as_view(), name='airports-all'),
    url('airports/$', ListAirportView.as_view(), name='airports-all'),
    url('^airports/name/(?P<airport_name>[\w-]+)/$', AirportNameListView.as_view(), name="airports-name-list"),
    url('^airports/iata/(?P<airport_iata>[\w-]+)/$', AirportIATADetailView.as_view(), name="airports-iata-detail"),

]
