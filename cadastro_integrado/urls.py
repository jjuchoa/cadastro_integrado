from django.urls import path

from django.contrib import admin

from pais.views import PaisListView, PaisCreateView, PaisUpdateView
from estado.views import EstadoListView, EstadoCreateView, EstadoUpdateView
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('paislist/', PaisListView.as_view(), name='pais_list'),
    path('paisadd/', PaisCreateView.as_view(), name='pais_add'),
    path('<int:pk>/paisedit/', PaisUpdateView.as_view(), name='pais_edit'),
    path('estadolist/', EstadoListView.as_view(), name='estado_list'),
    path('estadoadd/', EstadoCreateView.as_view(), name='estado_add'),
    path('<int:pk>/estadoedit/', EstadoUpdateView.as_view(), name='estado_edit'),
    path('admin/', admin.site.urls),
]
