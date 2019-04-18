from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Cities
from .serializers import CitySerializer
from city.forms import CForm
from django.shortcuts import redirect
from django.http import HttpResponse




def city(request):
    message = ""
    if request.method == "POST":
        ncform = CForm(request.POST)
        if ncform.is_valid():
            ncity = ncform.cleaned_data['cname']
            rstatus = ncform.cleaned_data['rstatus']
            city = Cities(name = ncity, pcity = "", status = rstatus)
            city.save()
    else:
        ncform = CForm()
    cities = Cities.objects.all()
    if cities:
        lcity = cities.order_by("-id")[0]
    else :
        lcity = "None"
    return render(request,'templates/City.html', {"cities" : cities, "lastname": lcity, "message" : message})

def delete(request):
    cities = Cities.objects.all()
    if cities:
        cities.order_by("-id")[0].delete()
    return redirect(city)


def deleteall(request):
    cities = Cities.objects.all()
    cities.delete()
    return redirect(city)


class ListCityView(generics.ListAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitySerializer
