# coding=utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .managers import AirportSet


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

    slug = models.SlugField(_('slug'), max_length=255,
                            help_text=_("Used to build the URL of the airport "
                                        "and also to search by airports name."))

    iata = models.CharField(_('IATA'), max_length=255, blank=True)

    icao = models.CharField(_('ICAO'), max_length=255, blank=True)

    city = models.CharField(_('city'), max_length=255, blank=True)

    country = models.CharField(_('city'), max_length=255, blank=True)

    latitude = models.FloatField(_('latitude'), blank=True)

    longitude = models.FloatField(_('longitude'), blank=True)

    objects = AirportSet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Airport')
        verbose_name_plural = _('Airports')
