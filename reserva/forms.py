from django import forms
from .models import Hotel, Reserva

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
