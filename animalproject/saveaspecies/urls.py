from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from saveaspecies.views import *


urlpatterns = [
    path("home/", Homeview.as_view() , name="home"), 
    path("", Landingview.as_view() , name="landing"),
    path("animalspecies/  ", Animalspeciesview.as_view() , name="species"),
    path("animaltype/", Animalspeciesview.as_view() , name="species"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)