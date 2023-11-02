from . import views
from django.urls import path, re_path, register_converter
from . import convertors


register_converter(convertors.FourDigitYearConverter, "year4")

urlpatterns = [

    path('', views.index),
    path('story/<int:car_id>', views.categories),
    path('story/<slug:car_slug>/', views.categories_bu_slug),
    path("archive/<year4:year>/",views.archive),

]
