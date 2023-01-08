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