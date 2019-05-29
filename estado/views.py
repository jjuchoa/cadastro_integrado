from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from estado.models import Estado


class EstadoListView(ListView):
    model = Estado
    context_object_name = 'estado'


class EstadoCreateView(CreateView):
    model = Estado
    fields = ('nome', 'pais')
    success_url = reverse_lazy('estado_list')


class EstadoUpdateView(UpdateView):
    model = Estado
    fields = ('nome', 'pais')
    template_name = 'estado/estado_update_form.html'
    success_url = reverse_lazy('estado_list')


class EstadoDeleteView(DeleteView):
    model = Estado
    template_name = 'estado/estado_delete_form.html'
    success_url = reverse_lazy('estado_list')
