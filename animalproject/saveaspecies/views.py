from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View


class Landdingpageview(View):
    def get(self, request):
        return render( request=request , template_name = "saveaspecies/landingpage.html", context = {})

class Homeview(View):
    def get(self, request):
        return render( request=request , template_name = "saveaspecies/home.html", context = {})