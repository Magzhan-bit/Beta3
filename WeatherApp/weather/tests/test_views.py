from django.test import TestCase, Client
from django.urls import reverse
from weather.models import City

class TestViews(TestCase):

    def test_Daymode_Post(self):
        client = Client()

        response = client.get(reverse('Day mode'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Daymode.html')

    def test_Nightmode_Post(self):
        client = Client()

        response = client.get(reverse('Night mode'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Nightmode.html')

    def test_loginPage_Post(self):
        client = Client()

        response = client.get(reverse('login'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_Homepage_Post(self):
        client = Client()

        response = client.get(reverse('Home page'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Homepage.html')

    def test_registerPage_Post(self):
        client = Client()

        response = client.get(reverse('register'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_about_us_Post(self):
        client = Client()

        response = client.get(reverse('about'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')