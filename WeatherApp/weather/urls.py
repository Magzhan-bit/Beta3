from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
    path('Homepage', views.Homepage, name='Home page'),
    path('Nightmode', views.Nightmode, name='Night mode'),
    path('Daymode', views.Daymode, name='Day mode'),
    path('about_us', views.about_us, name='about'),
]
