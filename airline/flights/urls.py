from django.urls import path

from . import views

app_name = "flightapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("book/<int:flight_id>", views.book, name="book"),
    path("search", views.search, name="search"),
]
