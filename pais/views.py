from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from pais.models import Pais


class PaisListView(ListView):
    model = Pais
    context_object_name = 'pais'


class PaisCreateView(CreateView):
    model = Pais
    fields = ('codPais', 'nome')
    success_url = reverse_lazy('pais_list')


class PaisUpdateView(UpdateView):
    model = Pais
    fields = ('codPais', 'nome')
    template_name = 'pais/pais_update_form.html'
    success_url = reverse_lazy('pais_list')


class PaisDeleteView(DeleteView):
    model = Pais
    template_name = 'pais/pais_delete_form.html'
    success_url = reverse_lazy('pais_list')
