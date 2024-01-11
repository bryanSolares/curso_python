from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
                  path('', views.inicio, name='inicio'),
                  path('nosotros/', views.nosotros, name='nosotros'),
                  path('clientes/', views.clientes, name='clientes'),
                  path('clientes/crear', views.crear, name='crear'),
                  path('clientes/eliminar/<int:id>', views.eliminar, name='eliminar'),
                  path('clientes/editar/<int:id>', views.editar, name='editar')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
