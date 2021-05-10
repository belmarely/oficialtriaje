import self as self
from django import forms
from Models.triaje.models import Usuaria, Funcionaria, Diagnostico, Entrada, Salida
from django.forms import ValidationError


class formularioUsuaria(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=100)
    apellido = forms.CharField(min_length=3, max_length=100)
    identidad = forms.CharField(min_length=13, max_length=15)

    def clean_identidad(self):
        identidad = self.cleaned_data['identidad']
        existe = Usuaria.objects.filter(identidad__iexact=identidad).exists()

        if existe:
            raise ValidationError('Ya existe número de indentidad')
        return identidad

    class Meta:
        model = Usuaria
        fields = ('nombre', 'apellido', 'identidad', 'celular', 'identidad_funcionaria',)


# MODELO Agregar funcionaria
class formularioFuncionaria(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=100)
    apellido = forms.CharField(min_length=3, max_length=100)
    identidad = forms.CharField(min_length=13, max_length=15)

    def clean_identidad(self):
        identidad = self.cleaned_data['identidad']
        existe = Usuaria.objects.filter(identidad__iexact=identidad).exists()

        if existe:
            raise ValidationError('Identidad de Usuaria existente')
        return identidad

    class Meta:
        model = Funcionaria
        fields = ('nombre', 'apellido', 'identidad', 'celular', 'id_modulo', 'identidad_funcionaria',)


# MODELO Agregar Diagostico
class formularioDiagnostico(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ('id_usuaria', 'temperatura', 'sintomas', 'contacto',)


# MODELO Agregar Diagostico Funcionaria
class formularioDiagnosticoFuncionaria(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ('id_funcionaria', 'temperatura', 'sintomas', 'contacto',)


# Modelo Agregar entrada Usuaria
class formularioEntradaUsuaria(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ('id_usuaria', 'hora', 'fecha', 'descripcion',)
        widgets = {'hora': forms.TimeInput(attrs={'type': 'time'}), 'fecha': forms.DateInput(attrs={'type': 'date'})}


# Modelo Agregar salida Usuaria
class formularioSalidaUsuaria(forms.ModelForm):
    class Meta:
        model = Salida
        fields = ('id_usuaria', 'hora', 'fecha',)
        widgets = {'hora': forms.TimeInput(attrs={'type': 'time'}), 'fecha': forms.DateInput(attrs={'type': 'date'})}


# Modelo Agregar entrada Funcionaria
class formularioEntradaFuncionaria(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ('id_funcionaria', 'hora', 'fecha',)
        widgets = {'hora': forms.TimeInput(attrs={'type': 'time'}), 'fecha': forms.DateInput(attrs={'type': 'date'})}


# Modelo Agregar salida Funcionaria
class formularioSalidaFuncionaria(forms.ModelForm):
    class Meta:
        model = Salida
        fields = ('id_funcionaria', 'hora', 'fecha', 'temperatura1',)
        widgets = {'hora': forms.TimeInput(attrs={'type': 'time'}), 'fecha': forms.DateInput(attrs={'type': 'date'})}
