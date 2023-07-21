from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Airport, Passenger, Flight


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html")
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all(),
        "city": Airport.objects.all()
    })


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "Flight": flight,
        "Passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })


def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        new_passenger = Passenger(first_name=first_name, last_name=last_name)
        new_passenger.save()
        flight.passengers.add(new_passenger)
        return HttpResponseRedirect(reverse('flightapp:index'))
    else:
        return render(request, "users/book.html", {
            "flightid": flight_id
        })


def search(request):
    if request.method == "POST":
        start_code = request.POST.get('from')
        stop_code = request.POST.get('destination')
        flightslist = Flight.objects.filter(origin__code=start_code, destination__code=stop_code)
        return render(request, "flights/searchresult.html", {
            "flightslist": flightslist
        })
