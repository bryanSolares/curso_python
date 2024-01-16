from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente
from .forms import ClienteForm

# Create your views here.
def inicio(request):
    return render(request,'generales/inicio.html')

def nosotros(request):
    return render(request,'generales/nosotros.html')

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request,'crud/lista.html', {"data": clientes})

def crear(request):
    formulario = ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("clientes")
    return render(request, 'crud/crear.html', {'formulario': formulario})

def eliminar(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect("clientes")

def editar(request, id):
    cliente = Cliente.objects.get(id=id)
    formulario = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect("clientes")
    return render(request, 'crud/editar.html', {'formulario': formulario})