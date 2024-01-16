from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

app_name = 'clientes_app'

urlpatterns = [
                  path("", views.Inicio.as_view(), name="inicio"),
                  path("lista_clientes", views.ListaClientes.as_view(), name="lista_clientes"),
                  path("crear_cliente", views.CrearCliente.as_view(), name="crear_cliente"),
                  path("editar_cliente/<pk>", views.EditarCliente.as_view(), name="editar_cliente"),
                  path("eliminar_cliente/<pk>", views.EliminarCliente.as_view(), name="eliminar_cliente")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
