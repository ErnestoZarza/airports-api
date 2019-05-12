# coding=utf-8
import csv
import io

from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from django.template.defaultfilters import slugify

from .models import Airport
from .serializer import AirportSerializer


class ListAirportView(generics.ListAPIView):
    """
    Provides a list of  Airports.
    """
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

    def get_paginated_response(self, data):
        return Response(data)


class AirportNameListView(generics.ListAPIView):
    """
    Provides a list of  Airports filtered by name.
    """

    serializer_class = AirportSerializer

    def get_queryset(self):
        """
        Queryset method
        """

        slug_pattern = slugify(self.kwargs['airport_name'])

        # queryset = Airport.objects.search_by_name(airport_name)
        queryset = Airport.objects.filter(slug__icontains=slug_pattern).distinct()
        return queryset

    def get_paginated_response(self, data):
        return Response(data)


#

class AirportIATADetailView(generics.RetrieveAPIView):
    """
        GET Airport/:id/

    """
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

    def get(self, request, *args, **kwargs):
        try:
            iata = str(kwargs["airports_iata"]).upper()
            airports = self.queryset.get(iata=iata)
            return Response(AirportSerializer(airports).data)
        except Airport.DoesNotExist:
            return Response(
                data={
                    "message": "The Airport with IATA: {} does not exist".format(kwargs["airports_iata"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


@permission_required('admin.can_add_log_entry')
def upload_data(request):
    """
    This is the view to upload the CSV file and store the data
    :param request:
    :return: the render of the view
    """

    template = 'data_upload.html'

    """	"""

    prompt = {'order': 'The order of the CSV according to "OurAirports.com" should be: '
                       'id, ident, type, name, latitude_deg, longitude_deg, elevation_ft, '
                       'continent, iso_country, iso_region, municipality, scheduled_service, '
                       'gps_code, iata_code, local_code, home_link, wikipedia_link, keywords'
              }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'The file is not a CSV file')

    data_set = csv_file.read().decode('UTF-8')
    io_s = io.StringIO(data_set)
    next(io_s)

    csv_reader = csv.reader(io_s, delimiter=',')

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

    # variables to set the final data to the assets
    name = ""
    iata = ""
    icao = ""
    city = ""
    country = ""
    latitude = 0
    longitude = 0

    messages.add_message(request, messages.get_level(request), "loading the data!\n")

    for row in csv_reader:
        if not row[13]:
            continue

        name = row[3]
        slug = slugify(name)
        iata = row[13]
        icao = row[12]
        city = row[10]
        country = row[8]
        latitude = row[4]
        longitude = row[5]

        try:

            airport, created = Airport.objects.get_or_create(name=name, iata=iata, icao=icao,
                                                             city=city, latitude=latitude,
                                                             longitude=longitude, country=country,
                                                             slug=slug)

            if created:
                airport.save()

        except Exception as ex:
            messages.error(request, "\n\nSomething went wrong saving this Airport: {}\n{}".format(name, str(ex)))

    context = {}

    messages.add_message(request, messages.get_level(request), "The file was successfully uploaded!\n")

    messages.add_message(request, messages.get_level(request), "Please, check the API or the Administration site "
                                                               "to retrieve the data, "
                                                               "or go back to upload another file.")

    return render(request, template, context)
