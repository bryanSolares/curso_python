from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
                  path("", views.inicio, name="inicio"),
                  path("clientes/lista", views.lista_clientes, name="lista_clientes"),
                  # path("clientes_crear/", views.crear_editar_cliente, name="crear_editar_cliente")
                  path("<int:id>/", views.crear_editar_cliente, name="crear_editar_cliente"),
                  path("eliminar/<int:id>/", views.eliminar_cliente, name="eliminar_cliente")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
