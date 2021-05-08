"""triajeccmlc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Models.triaje.views import formularioUsuariaView, formularioDiagnosticoView, formularioFuncionariaView, \
    formularioDiagnosticoFView, formularioEntradaUsuariaView,  \
    formularioSalidaFuncionariaView, formularioEntradaFuncionariaView
from homeView.homeViews import homeViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeViews.index, name='Home'),
    path('usuaria/', homeViews.usuaria, name='Usuaria'),
    path('funcionaria/', homeViews.funcionaria, name='Funcionaria'),
    path('registrarUsuaria/', formularioUsuariaView.index, name='registrarUsuaria'),
    path('guardarUsuaria/', formularioUsuariaView.procesar_formulario, name='guardarUsuaria'),
    path('listarUsuaria/', formularioUsuariaView.listarUsuarias, name='listarUsuaria'),
    path('registrarDiagnostico', formularioDiagnosticoView.index, name='registrarDiagnostico'),
    path('guardarDiagnostico/', formularioDiagnosticoView.procesar_formulario, name='guardarDiagnostico'),
    path('registrarFuncionaria/', formularioFuncionariaView.index, name='registrarFuncionaria'),
    path('guardarFuncionaria/', formularioFuncionariaView.procesar_funcionaria, name='guardarFuncionaria'),
    path('listarFuncionaria/', formularioFuncionariaView.listarFuncionarias, name='listarFuncionaria'),
    path('registrarDiagnosticoFuncionaria', formularioDiagnosticoFView.index, name='registrarDiagnosticoFuncionaria'),
    path('guardarDiagnosticoFuncionaria/', formularioDiagnosticoFView.procesar_formulario,
         name='guardarDiagnosticoFuncionaria'),
    path('registrarEntradaUsuaria/', formularioEntradaUsuariaView.index, name='registrarEntradaUsuaria'),
    path('guardarEntradaUsuaria/', formularioEntradaUsuariaView.procesar_formulario, name='guardarEntradaUsuaria'),
    path('registrarEntradaFuncionaria/', formularioEntradaFuncionariaView.index, name='registrarEntradaFuncionaria'),
    path('guardarEntradaFuncionaria/', formularioEntradaFuncionariaView.procesar_formulario,
         name='guardarEntradaFuncionaria'),
    path('registrarSalidaFuncionaria/', formularioSalidaFuncionariaView.index, name='registrarSalidaFuncionaria'),
    path('guardarSalidaFuncionaria/', formularioSalidaFuncionariaView.procesar_formulario,
         name='guardarSalidaFuncionaria'),
]
