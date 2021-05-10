from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from Models.triaje.form import formularioUsuaria, formularioFuncionaria, formularioDiagnostico, \
    formularioDiagnosticoFuncionaria, formularioEntradaUsuaria, formularioSalidaUsuaria, formularioEntradaFuncionaria, \
    formularioSalidaFuncionaria
from Models.triaje.models import Usuaria, Funcionaria, Diagnostico, Entrada, Salida


class formularioUsuariaView(HttpRequest):

    def index(request):
        usuaria = formularioUsuaria()
        return render(request, "nuevaUsuaria.html", {'form': usuaria})

    def procesar_formulario(request):
        usuaria = formularioUsuaria(request.POST)
        if usuaria.is_valid():
            usuaria.save()
            usuaria = formularioUsuaria()

        return render(request, "usuaria.html", {'form': usuaria, 'mensaje': 'Ok'})


    # TRAER DATOS
    def listarUsuarias(request):
        queryset = request.GET.get("buscar")
        usuarias = Usuaria.objects.all()
        entradas = Entrada.objects.all()
        diagnosticos = Diagnostico.objects.all()
        if queryset:
            usuarias = Usuaria.objects.filter(
                Q(identidad__icontains=queryset)
            ).distinct()
            entradas = Entrada.objects.filter(
                Q(id_usuaria__identidad__contains=queryset)
            ).distinct()
            diagnosticos = Diagnostico.objects.filter(
                Q(id_usuaria__identidad__contains=queryset)
            ).distinct()
        return render(request, "listarUsuaria.html", {'usuarias': usuarias, 'entradas': entradas, 'diagnosticos': diagnosticos})


class formularioFuncionariaView(HttpRequest):

    def index(request):
        funcionaria = formularioFuncionaria()
        return render(request, "nuevaFuncionaria.html", {'form': funcionaria})

    def procesar_funcionaria(request):
        funcionaria = formularioFuncionaria(request.POST)
        if funcionaria.is_valid():
            funcionaria.save()
            funcionaria = formularioFuncionaria()

            return render(request, "nuevaFuncionaria.html", {'form': funcionaria, 'mensaje': 'Ok'})

    # TRAER DATOS
    def listarFuncionarias(request):
        queryset = request.GET.get("buscar")
        funcionarias = Funcionaria.objects.all()
        entradas = Entrada.objects.all()
        salidas = Salida.objects.all()
        diagnosticos = Diagnostico.objects.all()
        if queryset:
            funcionarias = Funcionaria.objects.filter(
                Q(identidad__icontains=queryset)
            ).distinct()
            entradas = Entrada.objects.filter(
                Q(id_funcionaria__identidad__icontains=queryset)
            ).distinct()
            salidas = Salida.objects.filter(
                Q(id_funcionaria__identidad__icontains=queryset)
            ).distinct()
            diagnosticos = Diagnostico.objects.filter(
                Q(id_funcionaria__identidad__icontains=queryset)
            ).distinct()
        return render(request, "listarFuncionaria.html", {'funcionarias': funcionarias, 'entradas': entradas, 'salidas': salidas, 'diagnosticos': diagnosticos})


class formularioDiagnosticoView(HttpRequest):
    def index(request):
        diagnostico = formularioDiagnostico()
        return render(request, "bioseguridadUsuaria.html", {'form': diagnostico})

    def procesar_formulario(request):
        diagnostico = formularioDiagnostico(request.POST)
        if diagnostico.is_valid():
            diagnostico.save()
            diagnostico = formularioDiagnostico()

        return render(request, "Usuaria.html", {'form': diagnostico, 'mensaje': 'Ok'})


class formularioDiagnosticoFView(HttpRequest):
    def index(request):
        diagnosticoF = formularioDiagnosticoFuncionaria()
        return render(request, "bioseguridadFuncionaria.html", {'form': diagnosticoF})

    def procesar_formulario(request):
        diagnosticoF = formularioDiagnosticoFuncionaria(request.POST)
        if diagnosticoF.is_valid():
            diagnosticoF.save()
            diagnosticoF = formularioDiagnosticoFuncionaria()

        return render(request, "listarFuncionaria.html", {'form': diagnosticoF, 'mensaje': 'Ok'})


class formularioEntradaUsuariaView(HttpRequest):
    def index(request):
        entradaU = formularioEntradaUsuaria()
        return render(request, "usuaria.html", {'form': entradaU})

    def procesar_formulario(request):
        entradaU = formularioEntradaUsuaria(request.POST)
        if entradaU.is_valid():
            entradaU.save()
            entradaU = formularioEntradaUsuaria()

        return render(request, "usuaria.html", {'form': entradaU, 'mensaje': 'Ok'})


class formularioEntradaFuncionariaView(HttpRequest):
    def index(request):
        entradaF = formularioEntradaFuncionaria()
        return render(request, "funcionaria.html", {'form': entradaF})

    def procesar_formulario(request):
        entradaF = formularioEntradaFuncionaria(request.POST)
        if entradaF.is_valid():
            entradaF.save()
            entradaF = formularioEntradaFuncionaria

        return render(request, "funcionaria.html", {'form': entradaF, 'mensaje': 'Ok'})

class formularioSalidaFuncionariaView(HttpRequest):
    def index(request):
        salidaF = formularioSalidaFuncionaria()
        return render(request, "funcionaria.html", {'form': salidaF})

    def procesar_formulario(request):
        salidaF = formularioSalidaFuncionaria(request.POST)
        if salidaF.is_valid():
            salidaF.save()
            salidaF = formularioSalidaFuncionaria()

        return render(request, "funcionaria.html", {'form': salidaF, 'mensaje': 'Ok'})
