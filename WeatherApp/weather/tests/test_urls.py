from django.test import SimpleTestCase
from django.urls import reverse, resolve
from weather.views import Nightmode, Daymode, Homepage, about_us, logoutUser, loginPage, registerPage

class TestUrls(SimpleTestCase):

    def test_Nightmode_url_resolves(self):
        url = reverse('Night mode')
        self.assertEquals(resolve(url).func, Nightmode)

    def test_Daymode_url_resolves(self):
        url = reverse('Day mode')
        self.assertEquals(resolve(url).func, Daymode)

    def test_Homepage_url_resolves(self):
        url = reverse('Home page')
        self.assertEquals(resolve(url).func, Homepage)

    def test_about_us_url_resolves(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about_us)

    def test_logoutUser_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutUser)

    def test_loginPage_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginPage)

    def test_registerPage_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, registerPage)