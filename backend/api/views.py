from django.shortcuts import render
from rest_framework import viewsets
from .models import *
#from .serializers import *
from django.core import serializers
from django.http import HttpResponse
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# Create your views here.
###############################----Métodos de Create--------#############################################
#creacion de país
def addCountry(request,id,code,name,language,date,update,enable,user):
    try:
        country=Countrycode.create(id,code,name,language,date,update,enable,user)
        country.save()
    except Exception as e:
        print(e)
        return HttpResponse("Fallo",status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("Correcto", status=status.HTTP_200_OK)

#creacion de campus
def addCampus(request,id,name,sname,instid,language,date,update,enabled,userid):
    try:
        campus=Campus.create(id,name,sname,instid,language,date,update,enabled,userid)
        campus.save()
    except Exception as e:
        print(e)
        return HttpResponse("Fallo",status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("Correcto", status=status.HTTP_200_OK)

#creacion de ciudades
def addCity(request,id,city,name,countryid,language,date,update,enabled,userid):
    try:
        city=Citycode.create(id,city,name,countryid,language,date,update,enabled,userid)
        city.save()
    except Exception as e:
        print(e)
        return HttpResponse("Fallo",status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("Correcto", status=status.HTTP_200_OK)

#creacion de estatus académico
def addAcademicStatus(request,id,name,sname,instid,language,date,update,enabled,userid):
    try:
        academic=Academicstatus.create(id,name,sname,instid,language,date,update,enabled,userid)
        academic.save()
    except Exception as e:
        print(e)
        return HttpResponse("Fallo",status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("Correcto", status=status.HTTP_200_OK)

#creacion de medios de contacto
def addContactMedia(request,id,name,language,date,update,enabled,userid):
    try:
        contact=Contactmedia.create(id,name,language,date,update,enabled,userid)
        contact.save()
    except Exception as e:
        print(e)
        return HttpResponse("Fallo",status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("Correcto", status=status.HTTP_200_OK)

##########-------------------Métodos de lectura,obtencion------------###############
#obtencion de paises
def allCountry(request):
    allCountry=Countrycode.objects.all()
    serialized_object=serializers.serialize('json',allCountry)
    return HttpResponse(serialized_object, content_type='text/json')

#obtencion de campus
def allCampus(request):
    allCampus=Campus.objects.all()
    serialized_object=serializers.serialize('json',allCampus)
    return HttpResponse(serialized_object, content_type='text/json')
#obtencion de ciudades
def allCity(request):
    allCity=Citycode.objects.all()
    serialized_object=serializers.serialize('json',allCity)
    return HttpResponse(serialized_object, content_type='text/json')
#obtencion de estatus academico
def allAcademicStatus(request):
    allAcademicStatus=Academicstatus.objects.all()
    serialized_object=serializers.serialize('json',allAcademicStatus)
    return HttpResponse(serialized_object, content_type='text/json')
##########--------------Métodos de borrado lógico-------######################
#borrar pais
def deleteCountry(request,iden):
    try:
        country=Countrycode.objects.get(idcountrycode=iden)
        country.enabled=False
        country.save()
    except Exception as e:
        print(e)
        return HttpResponse("Fallo", status = status.HTTP_400_BAD_REQUEST)
    return HttpResponse("Correcto", status=status.HTTP_200_OK)

#borrar campus
def deleteCampus(request,iden):
    try:
        campus=Campus.objects.get(idcampus=iden)
        campus.enabled=False
        campus.save()
    except Exception as e:
        print(e)
        return HttpResponse("Fallo", status = status.HTTP_400_BAD_REQUEST)
    return HttpResponse("Correcto", status=status.HTTP_200_OK)

#borrar ciudad
def deleteCity(request,iden):
    try:
        city=Citycode.objects.get(idcitycode=iden)
        city.enabled=False
        city.save()
    except Exception as e:
        print(e)
        return HttpResponse("Fallo", status = status.HTTP_400_BAD_REQUEST)
    return HttpResponse("Correcto", status=status.HTTP_200_OK)

#borrar estatus académico
def deleteAcademicStatus(request,iden):
    try:
        academic=Academicstatus.objects.get(idacademicstatus=iden)
        academic.enabled=False
        academic.save()
    except Exception as e:
        print(e)
        return HttpResponse("Fallo", status = status.HTTP_400_BAD_REQUEST)
    return HttpResponse("Correcto", status=status.HTTP_200_OK)
#################--------Métodos de actualización-------------#####################
#actualizacion de paises
def updateCountry(request,id,incod,code,name,language,update,enable,user):
    try:
        country=Countrycode.objects.get(idcountrycode=id)
        country.internalcode=incod
        country.countrycode=code
        country.countryname=name
        country.languagecode=language
        country.updateddate=update
        country.enabled=enable
        country.userid=user
        country.save()
    except Exception as e:
        print(e)        
        return HttpResponse("Incorrecto", status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("Correcto", status=status.HTTP_200_OK)

# #actualizacion de Campus
def updateCampus(request,id,interid,name,sname,instid,language,date,update,enabled,userid):
    try:
        campus=Campus.objects.get(idcampus=id)
        campus.internalcode=interid
        campus.campusname=name
        campus.campusshortname=sname
        campus.instituteid=instid
        campus.languagecode=language
        campus.createddate=date
        campus.updateteddate=update
        campus.enabled=enabled
        campus.userid=userid
        campus.save()
    except Exception as e:
        print(e)        
        return HttpResponse("Incorrecto", status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("Correcto", status=status.HTTP_200_OK)

#actualizacion de ciudad
def updateCity(request,id,interid,citycode,name,countryid,language,date,update,enabled,userid):
    try:
        city=Citycode.objects.get(idcitycode=id)
        city.internalcode=interid
        city.citycode=citycode
        city.cityname=name
        city.countrycodeid=countryid
        city.languagecode=language
        city.createddate=date
        city.updateddate=update
        city.enabled=enabled
        city.userid=userid
        city.save()
    except Exception as e:
        print(e)
        return HttpResponse("Incorrecto", status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("Correcto", status=status.HTTP_200_OK)

#actualizacion de estatus academico
def updateAcademicStatus(request,id,name,sname,instid,language,date,update,enabled,userid):
    try:
        academic=Academicstatus.objects.get(idacademicstatus=id)
        academic.academicstatusname=name
        academic.academicstatusshortname=sname
        academic.instituteid=instid
        academic.languagecode=language
        academic.createddate=date
        academic.updateddate=update
        academic.enabled=enabled
        academic.userid=userid
        academic.save()
    except Exception as e:
        print(e)
        return HttpResponse("Incorrecto",status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("Correcto",status=status.HTTP_200_OK)
#método de prueba para ver si hay acceso
def hola(request):
    print("hola")
    return HttpResponse("Correcto", status=status.HTTP_200_OK)