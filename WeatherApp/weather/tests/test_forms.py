from django.test import SimpleTestCase
from weather.forms import CreateUserForm, CityForm
from weather.models import City
from django.forms import TextInput
from django.contrib.auth.models import User

class TestForms(SimpleTestCase):
    def test_CreateUserForm(self):
        response = self.client.post("/my/form/", {'something': 'something'})
        self.assertEqual(response.status_code, 200)

class TestForms(SimpleTestCase):

    def test_CreateUserForm(self):
        form = CreateUserForm(data={})
        class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']

    def test_CityForm(self):
        form = CityForm(data={})
        class Meta:
            model = City
            fields = ['name']
            widgets = {'name' : TextInput(attrs={
                'class' : 'form-control',
                'name':'city',
                'id':'city',
                'placeholder':'Введите город'
                })}

    class TestForms(SimpleTestCase):
        def test_CreateUserForm(self):
            response = self.client.post("/my/form/", {'something': 'something'})
            self.assertEqual(response.status_code, 200)