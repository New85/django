from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

# Create your views here.

def index(reguest):
    return HttpResponse('Страница Car')

def categories(request, car_id):
    return HttpResponse(f"<h1>Страница HISTORIC CARS</h1><p>{car_id}</p>")

def categories_bu_slug(request, car_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Страница HISTORIC CARS</h1><p>slug:{car_slug}</p>")

def archive(request, year):
    if year > 2023:
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def page_not_found(request,exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

