from django.urls import path

from django.contrib import admin

from pais.views import PaisListView, PaisCreateView, PaisUpdateView


urlpatterns = [
    path('', PaisListView.as_view(), name='pais_list'),
    path('add/', PaisCreateView.as_view(), name='pais_add'),
    path('<int:pk>/edit/', PaisUpdateView.as_view(), name='pais_edit'),
    path('admin/', admin.site.urls),
]
