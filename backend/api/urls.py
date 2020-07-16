from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    #urls para agregar    
    path('addCountry/<id>/<code>/<name>/<language>/<date>/<update>/<enable>/<user>', addCountry),
    path('addCampus/<id>/<name>/<sname>/<instid>/<language>/<date>/<update>/<enabled>/<userid>',addCampus),
    path('addCity/<id>/<city>/<name>/<countryid>/<language>/<date>/<update>/<enabled>/<userid>',addCity),
    path('addAcademicStatus/<id>/<name>/<sname>/<instid>/<language>/<date>/<update>/<enabled>/<userid>',addAcademicStatus),
    path('addContactMedia/<id>/<name>/<language>/<date>/<update>/<enabled>/<userid>',addContactMedia),

    #urls para obtener
    path('getCountries',allCountry),
    path('getCampus',allCampus),
    path('getCity',allCity),
    path('getAcademicStatus',allAcademicStatus),

    #urls para borrar logicamente
    path('deleteCountry/<iden>',deleteCountry),
    path('deleteCampus/<iden>',deleteCampus),
    path('deleteCity/<iden>',deleteCity),
    path('deleteAcademicStatus/<iden>',deleteAcademicStatus),

    #urls para actualizar    
    path('updateCountry/<id>/<incod>/<code>/<name>/<language>/<update>/<enable>/<user>',updateCountry),  
    path('updateCampus/<id>/<interid>/<name>/<sname>/<instid>/<language>/<date>/<update>/<enabled>/<userid>',updateCampus),
    path('updateCity/<id>/<interid>/<citycode>/<name>/<countryid>/<language>/<date>/<update>/<enabled>/<userid>',updateCity),
    path('updateAcademicStatus/<id>/<name>/<sname>/<instid>/<language>/<date>/<update>/<enabled>/<userid>',updateAcademicStatus),
    path('hola',hola)
]