from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse

from .models import Cliente


# Create your views here.
class Inicio(TemplateView):
    template_name = 'generales/inicio.html'

class ListaClientes(ListView):
    template_name = 'crud/lista.html'
    model = Cliente
    ordering = '-nombre'
    queryset = Cliente.objects.all()
    context_object_name = 'data'

class CrearCliente(CreateView):
    template_name = 'crud/crear.html'
    model = Cliente
    fields = '__all__'

    def get_success_url(self, **kwargs):
        return reverse('clientes_app:lista_clientes')

class EditarCliente(UpdateView):
    template_name = 'crud/crear.html'
    model = Cliente
    fields = '__all__'
    pk_url_kwarg = 'pk'

    def get_success_url(self, **kwargs):
        return reverse('clientes_app:lista_clientes')


class EliminarCliente(DeleteView):
    template_name = 'crud/eliminar.html'
    model = Cliente
    pk_url_kwarg = 'pk'

    def get_success_url(self, **kwargs):
        return reverse('clientes_app:lista_clientes')