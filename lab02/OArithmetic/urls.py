from django.urls import path

from . import views

app_name = 'OArithmetic'

urlpatterns = [
    path('', views.calcular, name='calcular'),
    path('calculado/', views.calculado, name='calculado')
]