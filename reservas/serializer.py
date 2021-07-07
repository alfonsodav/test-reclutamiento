from rest_framework import serializers
from .models import *


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['estatus', 'duracion', 'cliente', 'habitaciones', 'fecha_entrada', 'fecha_salida']


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

    def create(self, data):
        reserva = Reserva.objects.get(fecha_entrada=str(data['reserva']))
        reserva.estatus = 'PAGADO'
        reserva.save()
        data['fecha'] = datetime.date.today()
        factura = Factura.objects.create(**data)
        self.context['factura'] = factura
        return self.context['factura']
