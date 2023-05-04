from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def agregarPerro(request):

    if request.method == 'GET':
        form = PerroForm()
        return render(request, 'agregarPerro.html', {
            'formulario': form
        })
    
    elif request.method == 'POST':
        form = PerroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Se guardo con exito!")

    return render(request, 'agregarPerro.html', {})

def agregarGato(request):

    if request.method == 'GET':
        form = GatoForm()
        return render(request, 'agregarGato.html', {
            'formulario': form
        })
    
    elif request.method == 'POST':
        form = GatoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Se guardo con exito!")

    return render(request, 'agregarGato.html', {})

def agregarPajaro(request):

    if request.method == 'GET':
        form = PajaroForm()
        return render(request, 'agregarPajaro.html', {
            'formulario': form
        })
    
    elif request.method == 'POST':
        form = PajaroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Se guardo con exito!")

    return render(request, 'agregarPajaro.html', {})


def buscar(request):

    info = request.GET.get('query')
    
    lista_de_perros = Perro.objects.filter(nombre__icontains=info)
    lista_de_gatos = Gato.objects.filter(nombre__icontains=info)
    lista_de_pajaros = Pajaro.objects.filter(nombre__icontains=info)

    return render(request, 'resultado_busqueda.html', {
        'perros': lista_de_perros,
        'gatos': lista_de_gatos,
        'pajaros': lista_de_pajaros,
    })