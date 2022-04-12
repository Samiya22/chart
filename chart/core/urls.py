from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('example/', example),
    path('imgchart/', imgchart),
    path('humans/', humans),
    path('telefonlar/', telefonlar),
    path('pie/', pie),
    path('statik/', statik),
    path('country/', country),
]
