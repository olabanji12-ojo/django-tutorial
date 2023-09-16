from django.template import loader
from django.http import HttpResponse
from .models import students
from .models import laptop
from .models import phones
from .models import cars
from .models import Car
from .models import Phone

def main(request):
   template = loader.get_template("main.html")
   return HttpResponse(template.render())

def products(request):
   template = loader.get_template("products.html")
   return HttpResponse(template.render())

def myapp(request):
    mystudents = laptop.objects.all().values()
    template =loader.get_template("text.html")
    context = {
          "mystudents": mystudents,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  mystudents = laptop.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mystudents': mystudents,
  }
  return HttpResponse(template.render(context, request))


def phone_to_choose(request):
   myphones = Phone.objects.all().values()
   template = loader.get_template("phone_to_choose.html")
   context = {
      "myphones" : myphones,
   }
   return HttpResponse(template.render(context, request))

def phones(request, id):
   myphones = Phone.objects.get(id=id)
   template = loader.get_template("phones.html")
   context = {
      "myphones" : myphones,
   }
   return HttpResponse(template.render(context, request))

def cars_to_buy(request):
    mycars = Car.objects.all().values()
    template = loader.get_template("cars_to_buy.html")
    context = {
        "mycars": mycars
    }
    return HttpResponse(template.render(context, request))

def cars(request, id):
    mycars = Car.objects.get(id=id)  # Use Car.objects.get instead of cars.objects.get
    template = loader.get_template("cars.html")
    context = {
        "mycars": mycars,  # Change mycars to mycar to represent a single car instance
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
