from django.db import models

# Create your models here.

#Residente(nombre, apellidos, fecha_nacimiento)
class Residente(models.Model):
    nombre=models.CharField("Nombre", max_length=50)
    apellidos=models.CharField("Apellidos", max_length=50)
    fecha_nacimiento=models.DateField("Fecha de Nacimiento ",auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Residente"
        verbose_name_plural = "Residentes"

    def __str__(self):
        return self.nombre
#Familiar(nombre, apellidos, fecha_nacimiento, parentesco)
class Familiar(models.Model):
    PADRE = 1
    MADRE = 2
    HIJO = 3
    HIJA = 4

    PARENTESCO_CHOICE = (
        (PADRE, 'Padre'),
        (MADRE, 'Madre'),
        (HIJO, 'Hijo'),
        (HIJA, 'Hija')
    )

    nombre=models.CharField("Nombre", max_length=50)
    apellidos=models.CharField("Apellidos", max_length=50)
    fecha_nacimiento=models.DateField("Fecha de nacimiento ",auto_now=False, auto_now_add=False)
    parentesco=models.PositiveSmallIntegerField("Parentesco", choices=PARENTESCO_CHOICE, default=PADRE)

    class Meta:
        verbose_name = "Familiar"
        verbose_name_plural = "Familiares"

    def __str__(self):
        return self.nombre
        
#Informe(fecha_informe, Partes[1..*])
class Informe(models.Model):
    nombre=models.CharField("Nombre", max_length=50, null=False, blank=False, default="Informe", unique=True)
    fecha_informe=models.DateField("Fecha de informe ",auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Informe"
        verbose_name_plural = "Informes"

    def __str__(self):
        return self.nombre
#ParteInforme(tipo, valoracion_inicial, objetivos, informe) 
class ParteInforme(models.Model):

    SANITARIA = 1
    FUNCIONAL = 2
    PSIQUICA = 3
    SOCIAL = 4
    TERAPIA_OCUPACIONAL = 5

    TIPO = (
        (SANITARIA, 'Sanitaria'),
        (FUNCIONAL, 'Funcional'),
        (PSIQUICA, 'Psiquica'),
        (SOCIAL, 'Social'),
        (TERAPIA_OCUPACIONAL, 'Terapia ocupacional')
    )
    tipo=models.PositiveSmallIntegerField("Tipo", choices=TIPO, default=SANITARIA)
    valoracion_inicial=models.TextField('Valoración',max_length=350,blank=True, null=True)
    objetivos=models.TextField("Objetivos", max_length=4000, blank=True, null=True)
    informe=models.ForeignKey(Informe, related_name="Informes", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Parte Informe"
        verbose_name_plural = "Partes Informes"

    def __str__(self):
        return str(self.informe)