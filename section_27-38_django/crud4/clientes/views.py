from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = 'clientes_app:login'
