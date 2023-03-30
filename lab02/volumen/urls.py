from django.urls import path

from . import views

app_name = 'volumen'

urlpatterns = [
    path('', views.volumen, name='volumen'),
    path('calcvolumen/', views.volumenCalculado, name='volumencalc')
]