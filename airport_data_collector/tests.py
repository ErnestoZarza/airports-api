from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.template.defaultfilters import slugify

from .models import Airport
from .serializer import AirportSerializer


# Create your tests here.

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_asset(name, iata, icao, city, country, latitude,
                     longitude):
        slug = slugify(name)
        Airport.objects.create(name=name, iata=iata, icao=icao,
                               city=city, country=country, latitude=latitude,
                               longitude=longitude, slug=slug)

    def setUp(self):
        # add test data
        self.create_asset("Berlin-Schönefeld International Airport", "SXF", "EDDB",
                          "Berlin", "DE", 52.380001068115, 13.522500038147)

        self.create_asset("Berlin-Tegel International Airport", "TXL", "EDDT",
                          "Berlin", "DE", 52.5597000122, 13.2876996994)

        self.create_asset("Berlin-Schönefeld Fake Airport", "SkF", "EDD",
                          "Berlin", "DE", 52.3800010681198, 13.522500038564)

        self.create_asset("Berlin-Tegel Fake Airport", "TEL", "EDDk",
                          "Berlin", "DE", 52.5597000122, 13.2876996994)


class GetAllAirportsTest(BaseViewTest):

    def test_get_all_airports(self):
        """
        This test ensures that all Airports added in the setUp method
        exist when we make a GET request to the airports / endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("airports-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Airport.objects.all()
        serialized = AirportSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAirportsNameTest(BaseViewTest):

    def test_get_airport_by_name(self):
        """
        This test ensures that all the Airports filtered by name added in the setUp method
        exist when we make a GET request to the airports/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("airports-name-list", kwargs={"version": "v1", "airport_name": "berlin"})
        )
        # fetch the data from db
        expected = Airport.objects.search_by_name("berlin")
        serialized = AirportSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAirportsIATATest(BaseViewTest):

    def test_get_airport_by_name(self):
        """
        This test ensures that all the Airports filtered by IATA added in the setUp method
        exist when we make a GET request to the airports/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("airports-iata-detail", kwargs={"version": "v1", "airport_iata": "txl"})
        )
        # fetch the data from db
        expected = Airport.objects.search_by_iata("TXL").first()
        serialized = AirportSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)