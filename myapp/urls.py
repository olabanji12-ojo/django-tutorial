from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("products/", views.products, name="products"),
    path("products/myapp/", views.myapp, name="myapp"),
    path("products/phone_to_choose/", views.phone_to_choose, name="phone_to_choose"),
    path("products/phone_to_choose/phones/<int:id>", views.phones, name="phones"),
    path("products/myapp/details/<int:id>", views.details, name="details"), # Fix the URL pattern here
    path("products/cars_to_buy/", views.cars_to_buy, name="cars_to_buy"),
    path("products/cars_to_buy/cars/<int:id>", views.cars, name="cars"),

]
