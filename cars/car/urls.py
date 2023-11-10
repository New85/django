from . import views
from django.urls import path, re_path, register_converter
from . import convertors


register_converter(convertors.FourDigitYearConverter, "year4")

urlpatterns = [

    path('', views.index, name='home'),  # http://127.0.0.1:8000/
    path('about/', views.about, name='about'),
    path('story/<int:car_id>', views.categories, name='car_id'),
    path('story/<slug:car_slug>/', views.categories_bu_slug),
    path("archive/<year4:year>/",views.archive),

]
