from django import forms
from Models.triaje.models import Usuaria, Funcionaria, Diagnostico, Entrada, Salida


class formularioUsuaria(forms.ModelForm):
    class Meta:
        model = Usuaria
        fields = ('nombre', 'apellido', 'identidad', 'celular', 'identidad_funcionaria',)


# MODELO Agregar funcionaria
class formularioFuncionaria(forms.ModelForm):
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
