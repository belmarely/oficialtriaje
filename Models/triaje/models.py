from django.db import models


class Usuaria(models.Model):
    identidad = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular = models.CharField(max_length=12, null=True, )
    identidad_funcionaria = models.CharField(max_length=13, default=None)

    def __str__(self):
        return self.identidad

class Funcionaria(models.Model):
    identidad = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular = models.CharField(max_length=12, null=True, )
    modulo_choices = (
        ('MSSR', 'MSSR'),
        ('MEC', 'MEC'),
        ('MAPRODEM', 'MAPRODEM'),
        ('MAA', 'MAA'),
        ('MAI', 'MAI'),
        ('MAE', 'MAE'),
        ('DN', 'DN'),
    )
    id_modulo = models.CharField(max_length=20, choices=modulo_choices)
    identidad_funcionaria = models.CharField(max_length=13, default=None)

    def __str__(self):
        return self.identidad


class Entrada(models.Model):
    id_usuaria = models.ForeignKey(Usuaria, null=True, blank=True, on_delete=models.CASCADE, default=None)
    id_funcionaria = models.ForeignKey(Funcionaria, null=True, blank=True, on_delete=models.CASCADE, default=None)
    hora = models.TimeField()
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200, null=True, default=None)


class Salida(models.Model):
    temperatura_choices = (
        ('Mayor 37.5ºC', 'Mayor o igual a 37.5ºC'),
        ('Menor 37.5ºC', 'Menor o igual a 37.5ºC'),
    )
    id_usuaria = models.ForeignKey(Usuaria, null=True, blank=True, on_delete=models.CASCADE, default=None)
    id_funcionaria = models.ForeignKey(Funcionaria, null=True, blank=True, on_delete=models.CASCADE, default=None)
    hora = models.TimeField()
    fecha = models.DateField()
    temperatura1 = models.CharField(max_length=30, choices=temperatura_choices, null=True, default=None)


class Diagnostico(models.Model):
    temperatura_choices = (
        ('Mayor 37.5ºC', 'Mayor o igual a 37.5ºC'),
        ('Menor 37.5ºC', 'Menor o igual a 37.5ºC'),
    )
    contacto_choices = (
        ('Caso sospechoso de COVID-19', 'Caso sospechoso de COVID-19'),
        ('Caso confirmado de COVID-19', 'Caso confirmado de COVID-19'),
        ('Ninguna de las anteriores', 'Ninguna de las anteriores'),
    )
    id_usuaria = models.ForeignKey(Usuaria, null=True, blank=True, on_delete=models.CASCADE, default=None)
    id_funcionaria = models.ForeignKey(Funcionaria, null=True, blank=True, on_delete=models.CASCADE, default=None)
    temperatura = models.CharField(max_length=30, choices=temperatura_choices)
    sintomas = models.CharField(max_length=500, default=None)
    contacto = models.CharField(max_length=100, choices=contacto_choices)
