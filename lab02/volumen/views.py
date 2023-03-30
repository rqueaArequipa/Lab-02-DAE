from django.shortcuts import render
import math

# Create your views here.
def volumen(request):
    return render(request, 'formulariovol.html')

def volumenCalculado(request):
    diametro = int(request.POST['diametro'])
    altura = int(request.POST['altura'])

    #Volumen
    volumen = math.pi * math.pow(diametro/2,2)*altura
    context = {
        'resultado': volumen,
        'titulo' : 'Volumen del cilindro'
    }
    return render(request, 'calculadovol.html', context)