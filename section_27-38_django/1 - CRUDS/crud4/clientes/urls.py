from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth import views as auth_views
from . import views

app_name = "clientes_app"

urlpatterns = [
                  path("", views.Home.as_view(), name="home"),
                  path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
                  path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name="logout")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
