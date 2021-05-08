from django.http import HttpResponse
from django.template.loader import get_template


class homeViews():
    def index(self):
        plantilla = get_template('index.html')
        return HttpResponse(plantilla.render())

    def usuaria(self):
        plantilla = get_template('usuaria.html')
        return HttpResponse(plantilla.render())

    def funcionaria(self):
        plantilla = get_template('funcionaria.html')
        return HttpResponse(plantilla.render())
