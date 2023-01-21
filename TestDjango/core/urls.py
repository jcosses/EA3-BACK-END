from django.urls import path
from .views import home, datos

urlpatterns = [
    path('',home,name="home.html"),
    path('datos',datos,name="datos.html"),
]