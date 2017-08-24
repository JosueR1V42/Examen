from django.db import models

# Create your models here.
class registro(models.Model):
    genero=(
            ('H','Hombre'),
            ('M','Mujer')
            )
    Nombre=models.CharField(max_length=50, help_text='Ingrese el nombre')
    Telefono=models.CharField(max_length=10, help_text='Ingrese el nombre')
    Sexo=models.CharField(max_length=1, help_text='Seleccione el sexo',choices=genero)
    Fecha_Nacimiento=models.DateField(help_text='Coloque la fecha de nacimiento')
