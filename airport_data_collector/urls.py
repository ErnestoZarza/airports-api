from django.conf.urls import url
from .views import ListAirportView, AirportNameDetailView, AirportIATADetailView, upload_data

urlpatterns = [
    url('airports/list', ListAirportView.as_view(), name='airports-all'),
    url('airports/', ListAirportView.as_view(), name='airports-all'),
    url(r'^(?P<airport_name>[\w-]+)/$', AirportNameDetailView.as_view(), name="airports-name-detail"),
    url(r'^(?P<airports_iata>[\w-]+)/$', AirportIATADetailView.as_view(), name="airports-iata-detail"),

]
