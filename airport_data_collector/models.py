# coding=utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


# Create your models here.

class Airport(models.Model):
    """
        Class that represents an airport and its information

        "name":"Berlin-Schönefeld International Airport",
        "iata":"SXF",
        "icao":"EDDB",
        "city":"Berlin",
        "country":"DE",
        "latitude":52.380001068115,
        "longitude":13.522500038147
    """

    name = models.CharField(_('name'), max_length=255)

    iata = models.CharField(_('IATA'), max_length=255, blank=True)

    icao = models.CharField(_('ICAO'), max_length=255, blank=True)

    city = models.CharField(_('city'), max_length=255, blank=True)

    latitude = models.FloatField(_('latitude'), blank=True)

    longitude = models.FloatField(_('longitude'), blank=True)
