from django.db import models

class students(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=150)
    school = models.CharField(max_length=200)
    dob = models.CharField(max_length=100)

class laptop(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    operating_system = models.CharField(max_length=100)

class phones(models.Model):
    manufacturer = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    battery_capacity = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)

class cars(models.Model):
    name = models.CharField(max_length=100)
    year_produced = models.CharField(max_length=100)
    price = models.CharField(max_length=150)

    
class Car(models.Model):
    name = models.CharField(max_length=100)
    year_produced = models.CharField(max_length=100)
    price = models.CharField(max_length=150)

class Phone(models.Model):
    manufacturer = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    battery_capacity = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)

    

# Create your models here.
