from django.urls import path
from home import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('about', views.about, name = 'about'),
    path('donate', views.donate, name = 'donate'),
    path('fooddonate', views.food, name = 'food'),
    path('moneydonate', views.money, name = 'money'),
    path('unsuscribe', views.unsuscribe, name = 'unsuscribe'),

]