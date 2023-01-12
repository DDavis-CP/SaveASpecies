from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View


class Homeview(View):
    def get(self, request):
        return render( request=request , template_name = "saveaspecies/home.html", context = {})


class Landingview(View):
    def get(self, request):
        return render( request=request , template_name = "saveaspecies/landing_page.html", context = {})

class Animalspeciesview(View):
    def get(self, request):
        return render( request=request , template_name = "saveaspecies/animal_species_page.html", context = {})

class Animaltypeview(View):
    def get(self, request):
        return render( request=request , template_name = "saveaspecies/animal_type_page.html", context = {})

class Searchview(View):
    def get(self, request):
        return render( request=request , template_name = "saveaspecies/search_page.html", context = {})

class Sourceview(View):
    def get(self, request):
        return render( request=request , template_name = "saveaspecies/source_page.html", context = {})