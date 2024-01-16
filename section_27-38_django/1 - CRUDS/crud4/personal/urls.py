from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = 'personal_app'

urlpatterns = [
                  path('', views.Inicio.as_view(), name='inicio'),
                  path('lista_personal/', views.ListaPersonal.as_view(), name='lista_personal'),
                  path('crear', views.CrearPersonal.as_view(), name='crear'),
                  path('editar/<int:pk>/', views.EditarPersonal.as_view(), name='editar'),
                  path('eliminar/<int:pk>/', views.EliminarPersonal.as_view(), name='eliminar'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
