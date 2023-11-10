from django.http import HttpResponse, HttpResponseNotFound, request
from django.shortcuts import redirect, render
from django.template.loader import render_to_string


# Create your views here.

menu =['Осайте', 'Добавить статью', 'Обратная связь', 'Войти']


class MyClass:
    def __int__(self,a , b):
        self.a = a
        self.b = b



def index(request):
    # t = render_to_string('car/index.html')  # путь к шаблону
    # return HttpResponse(t)
    data = {'titel': 'Главная страница',
            'menu': menu,
            'float': 255.25,
            'lst': [1,2,'abc', True],
            'set': {1,2,3,5},
            'dict': {'key1': 'value1', 'key2': 'value2'},
            'obj': MyClass(10,20)

            }
    return render(request,'car/index.html',context=data) # более удобный путь

def about(request):
    return render(request, 'car/about.html',{'titel': 'О сайте'})

def categories(request, car_id):
    return HttpResponse(f"<h1>Страница HISTORIC CARS</h1><p>{car_id}</p>")

def categories_bu_slug(request, car_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Страница HISTORIC CARS</h1><p>slug:{car_slug}</p>")

def archive(request, year):
    if year > 2023:

        return redirect('/') # перенаправление на главную страницу

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def page_not_found(request,exception):  # ошибка 404 более красивая
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

