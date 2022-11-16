from django.urls import path
from saveaspecies.views import *


urlpatterns = [
    path("home/", Homeview.as_view() , name="home"),
]