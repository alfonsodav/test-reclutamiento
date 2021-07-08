# test-reclutamiento
prueba de reclutamiento

Sistema se reservas a través de API muy simple, Integra registro 
de Hotel Propietario, Habitaciones con sus datos de piso, numero y 
tipo, Registro básico de cliente con su nombre y numero de 
identificación, Reserva que emplea los datos ya registrados con 
tres estados posibles (Pagado, Pendiente y Eliminado), Factura 
directamente enlazada con el dato de reserva y que al registrarse 
automáticamente cambia el estado de una reserva a Pagada. Al crearse una 
Reserva se calcula automáticamente el precio a pagar por la habitación

# lista de endPoint:
*  /hotel  : Para registrar los datos del hotel
*  /habitacion : para registrar los datos de la habitacion
*  /cliente  : para registrar al cliente
*  /reservar : Crea la reserva a partir de datos anteriores, El costo total se calcula a partir del costo diario de las 
habitaciones reservadas y la duracion de la estancia
*  /factura : simplemente registra fecha de pago de una reserva, incluye los datos del cliente, el hotel, metodo de pago y la reserva
tambien actualiza el estado de una reserva a PAGADO

Anexo: en el directorio test-front se incluyen capturas con sugerencias al estilo de la sección de ventas
