from django.db import models
import datetime
# Create your models here.


class Hotel(models.Model):
    nombre = models.CharField(null=False, max_length=20)
    direccion = models.CharField(null=False, max_length=30)
    id_fiscal = models.CharField(null=False, max_length=15)

    class Meta:
        verbose_name_plural = "Hotel"

    def __str__(self):
        return self.nombre


class Habitacion(models.Model):
    piso = models.IntegerField(null=False)
    numero = models.IntegerField(null=False)
    tipo = models.CharField('tipo de habitacion', max_length=15)

    class Meta:
        verbose_name_plural = "Habitaciones"

    def __str__(self):
        return 'h{} piso{}'.format(self.numero, self.piso)


class Cliente(models.Model):
    nombre = models.CharField(null=False, max_length=30)
    num_id = models.CharField(null=False, max_length=15)

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    opciones = [('PAGADO', 'pagado'), ('PENDIENTE', 'pendiente'), ('ELIMINADO', 'eliminado')]
    estatus = models.CharField(choices=opciones, default='PENDIENTE', max_length=10)
    duracion = models.PositiveIntegerField(null=False)
    habitaciones = models.ManyToManyField(Habitacion)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    fecha_entrada = models.DateField('Fecha de entrada')
    fecha_salida = models.DateField('Fecha de salida')

    def __str__(self):
        return str(self.fecha_entrada)


class Factura(models.Model):
    Hotel = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    reserva = models.ForeignKey(Reserva, on_delete=models.DO_NOTHING)
    fecha = models.DateField(auto_created=True, default=datetime.date.today(), blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.cliente.nombre, self.reserva)
