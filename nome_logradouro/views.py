from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from nome_logradouro.models import NomeLogradouro


class NomeLogradouroListView(ListView):
    model = NomeLogradouro
    context_object_name = 'nomelogradouro'


class NomeLogradouroCreateView(CreateView):
    model = NomeLogradouro
    fields = ('nome',)
    success_url = reverse_lazy('nomelogradouro_list')


class NomeLogradouroUpdateView(UpdateView):
    model = NomeLogradouro
    fields = ('nome',)
    template_name = 'nome_logradouro/nomelogradouro_update_form.html'
    success_url = reverse_lazy('nomelogradouro_list')


class NomeLogradouroDeleteView(DeleteView):
    model = NomeLogradouro
    template_name = 'nome_logradouro/nomelogradouro_delete_form.html'
    success_url = reverse_lazy('nomelogradouro_list')
