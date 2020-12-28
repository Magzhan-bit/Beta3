import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
from django.contrib.auth import authenticate, login, logout
from .forms import  CreateUserForm
from django.contrib import messages


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('Home page')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Учетная запись была создана для ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Home page')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('Home page')
            else:
                messages.info(request, 'Неверное имя пользователя или пароль')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def about_us(request):

    return render(request, 'about_us.html')

def Homepage(request):

    return render(request, 'Homepage.html')

def index(request):

    return render(request, 'index.html')

def Daymode(request):
    appid = '080b1c21833165c52b0250629455352f'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method=='POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        if res.get('main'):
            city_info = {
                'city': city.name,
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon'],
                'error': False,
            }
        else:
            city_info = {
                'city': city.name,
                'error': True,
            }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'Daymode.html', context)

def Nightmode(request):
    appid = '080b1c21833165c52b0250629455352f'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method=='POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        if res.get('main'):
            city_info = {
                'city': city.name,
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon'],
                'error': False,
            }
        else:
            city_info = {
                'city': city.name,
                'error': True,
            }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'Nightmode.html', context)
