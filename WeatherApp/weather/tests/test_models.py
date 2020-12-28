from django.test import TestCase
from weather.models import  City

class TestModels(TestCase):

    def setUp(self):
        self.City1 = City.objects.create(
            name = 'City1'
        )

    def test__str__(self):
        return self.City1