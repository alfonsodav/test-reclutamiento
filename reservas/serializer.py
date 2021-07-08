from rest_framework import serializers
from .models import *
import re


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

    def create(self, data):
        print(data)
        costos = 0
        duracion = data['duracion']
        habitaciones = data['habitaciones']
        for h in habitaciones:
            numero = re.search('[0-9]+', str(h)).group()
            habitacion = Habitacion.objects.get(numero=numero)
            costos = costos + habitacion.costo_dia * duracion

        data.pop('habitaciones')
        data['monto_pagar'] = costos
        reserva = Reserva.objects.create(**data)
        reserva.habitaciones.set(habitaciones)
        self.context['reserva'] = reserva
        return self.context['reserva']


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
