from django.contrib import admin
from .models import Hotel, Reserva
from .forms import HotelForm, ReservaForm


class HotelAdmin(admin.ModelAdmin):
    form = HotelForm


class ReservaAdmin(admin.ModelAdmin):
    form = ReservaForm


admin.site.register(Hotel, HotelAdmin)
admin.site.register(Reserva, ReservaAdmin)