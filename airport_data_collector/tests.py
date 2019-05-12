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
    def create_asset(name, iata, icao, city, latitude,
                     longitude, country):
        slug = slugify(name)
        Airport.objects.create(name=name, iata=iata, icao=icao,
                               city=city, latitude=latitude,
                               longitude=longitude, country=country,
                               slug=slug)

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


class GetAllAssetsTest(BaseViewTest):

    def test_get_all_assets(self):
        """
        This test ensures that all Assets added in the setUp method
        exist when we make a GET request to the assets/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("assets-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Airport.objects.all()
        serialized = AirportSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
