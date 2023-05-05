from django.shortcuts import render
from .models import Reserva


def home(request):
    return render(request, 'home.html')


def listado_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'listado_reservas.html', {'reservas': reservas})
