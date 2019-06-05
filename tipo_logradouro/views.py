from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from tipo_logradouro.models import TipoLogradouro


class TipoLogradouroListView(ListView):
    model = TipoLogradouro
    context_object_name = 'tipologradouro'


class TipoLogradouroCreateView(CreateView):
    model = TipoLogradouro
    fields = ('nome',)
    success_url = reverse_lazy('tipologradouro_list')


class TipoLogradouroUpdateView(UpdateView):
    model = TipoLogradouro
    fields = ('nome',)
    template_name = 'tipo_logradouro/tipologradouro_update_form.html'
    success_url = reverse_lazy('tipologradouro_list')


class TipoLogradouroDeleteView(DeleteView):
    model = TipoLogradouro
    template_name = 'tipo_logradouro/tipologradouro_delete_form.html'
    success_url = reverse_lazy('tipologradouro_list')
