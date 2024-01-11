from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

# Create your views here.
def inicio(request):
    return render(request, 'generales/inicio.html')


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'crud/lista.html', {'data': clientes})

'''
def crear_editar_cliente(request, id=0):
    if request.method == 'GET':
        formulario = ClienteForm()
        return render(request, 'crud/crear.html', {'formulario': formulario})
    else:
        formulario = ClienteForm(request.POST or None, request.FILES or None)
        if formulario.is_valid():
            formulario.save()
            return redirect("lista_clientes")
'''

def crear_editar_cliente(request, id=0):
    if request.method == 'GET':
        if id == 0:
            formulario = ClienteForm()
        else:
            cliente_id = Cliente.objects.get(pk=id)
            formulario = ClienteForm(instance=cliente_id)
        return render(request, 'crud/crear.html', {'formulario': formulario})
    else:
        if id == 0:
            formulario = ClienteForm(request.POST or None, request.FILES or None)
        else:
            cliente_id = Cliente.objects.get(pk=id)
            formulario = ClienteForm(request.POST or None, request.FILES or None, instance=cliente_id)

    if formulario.is_valid():
        formulario.save()
    return redirect("lista_clientes")

def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(pk=id)
    cliente.delete()
    return redirect("lista_clientes")