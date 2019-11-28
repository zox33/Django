from django.db import models

# Create your models here.


class Aeropuerto(models.Model):

    nombre= models.CharField(("Nombre"), max_length=50)
    ciudad= models.CharField(("Ciudad"), max_length=50)
    siglas= models.CharField(("Siglas"), max_length=50)

    class Meta:

        verbose_name= "Aeropuerto"
        verbose_name_plural= "Aeropuertos"
        ordering= ["nombre"]

    def __str__(self):
        return self.nombre


class Vuelo(models.Model):

    aeropuerto_salida= models.ForeignKey('Aeropuerto', verbose_name=("Aeropuerto Salida"),related_name="Aeropuerto_Llegada", on_delete=models.CASCADE)
    fecha_salida= models.DateField(("Fecha Salida"), auto_now=False, auto_now_add=False)
    fecha_llegada= models.DateField(("Fecha Llegada"), auto_now=False, auto_now_add=False)
    aeropuerto_llegada = models.ForeignKey('Aeropuerto', verbose_name=("Aeropuerto Llegada"),related_name="Aeropuerto_Salida", on_delete=models.CASCADE)
    codigo_vuelo = models.AutoField(("Codigo Vuelo"),primary_key=True)

    class Meta:
    
        verbose_name= "Vuelo"
        verbose_name_plural= "Vuelos"
        ordering= ["fecha_salida"]

    def __str__(self):
        return str(self.codigo_vuelo)


class Cliente(models.Model):

    nombre= models.CharField(("Nombre"), max_length=50)
    apellidos= models.CharField(("Apellidos"), max_length=50)
    email= models.EmailField(("Email"), max_length=254)
    fecha_nacimiento= models.DateField(("Fecha Nacimiento"), auto_now=False, auto_now_add=False)

    class Meta:
        
        verbose_name= "Cliente"
        verbose_name_plural= "Cliente"
        ordering= ["nombre"]

    def __str__(self):
        return self.nombre

class Reserva(models.Model):

    vuelo= models.ForeignKey('Vuelo',related_name="Vuelo", on_delete=models.CASCADE)
    cliente= models.ForeignKey('Cliente',related_name="Cliente", on_delete=models.CASCADE)
    fecha_reserva= models.DateField(("Fecha Reserva"), auto_now=False, auto_now_add=False)
    precio= models.DecimalField(("Precio"), max_digits=7, decimal_places=2)

    class Meta:
        
        verbose_name= "Reserva"
        verbose_name_plural= "Reservas"
        ordering= ["cliente","fecha_reserva"]

    def __str__(self):
        return str(self.cliente)