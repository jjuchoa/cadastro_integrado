from django.urls import path

from django.contrib import admin

from pais.views import PaisListView, PaisCreateView, PaisUpdateView, PaisDeleteView
from estado.views import EstadoListView, EstadoCreateView, EstadoUpdateView, EstadoDeleteView
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('paislist/', PaisListView.as_view(), name='pais_list'),
    path('paisadd/', PaisCreateView.as_view(), name='pais_add'),
    path('<int:pk>/paisedit/', PaisUpdateView.as_view(), name='pais_edit'),
    path('<int:pk>/paisdelete/', PaisDeleteView.as_view(), name='pais_delete'),
    path('estadolist/', EstadoListView.as_view(), name='estado_list'),
    path('estadoadd/', EstadoCreateView.as_view(), name='estado_add'),
    path('<int:pk>/estadoedit/', EstadoUpdateView.as_view(), name='estado_edit'),
    path('<int:pk>/estadodelete/', EstadoDeleteView.as_view(), name='estado_delete'),
    path('admin/', admin.site.urls),
]
