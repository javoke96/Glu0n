from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Cities
from .serializers import CitySerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_city(id="", name="", status=""):
        if id != "" and name !="" and status !="":
            Cities.objects.create(id=id,name=name,status=status)
    def setUp(self):
        self.create_city("1", "Istanbul", "1")
        self.create_city("2", "Ankara", "1")
        self.create_city("3", "Izmir", "0")

class GetAllCitiesTest(BaseViewTest):
    def test_get_all_cities(self):
        response = self.client.get(reverse("songs-all", kwargs={"version":"v1"}))
        expected = Cities.objects.all()
        serialized = CitySerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
