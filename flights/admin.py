from django.contrib import admin

from .models import Flight, Airport, Passengers

# Register your models here.
class Flight_Admin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class Passenger_Admin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight, Flight_Admin)
admin.site.register(Passengers, Passenger_Admin)
