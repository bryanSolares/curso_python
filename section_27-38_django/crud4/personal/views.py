from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .forms import PersonalForm
from django.urls import reverse


# Create your views here.
class Inicio(TemplateView):
    template_name = 'home-personal.html'


class ListaPersonal(ListView):
    template_name = 'lista-personal.html'
    model = Persona
    ordering = '-id'
    queryset = Persona.objects.all()
    context_object_name = 'data'


class CrearPersonal(CreateView):
    template_name = 'crear.html'
    model = Persona
    form_class = PersonalForm

    def get_success_url(self):
        return reverse('personal_app:lista_personal')


class EditarPersonal(UpdateView):
    template_name = 'crear.html'
    model = Persona
    form_class = PersonalForm
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse('personal_app:lista_personal')

class EliminarPersonal(DeleteView):
    template_name = 'eliminar.html'
    model = Persona
    pk_url_kwarg = 'pk'

    def get_success_url(self, **kwargs):
        return reverse('personal_app:lista_personal')