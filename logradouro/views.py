from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from logradouro.models import Logradouro


class LogradouroListView(ListView):
    model = Logradouro
    context_object_name = 'logradouro'


class LogradouroCreateView(CreateView):
    model = Logradouro
    fields = ('bairro', 'tipoLogradouro', 'nomeLogradouro')
    success_url = reverse_lazy('logradouro_list')


class LogradouroUpdateView(UpdateView):
    model = Logradouro
    fields = ('bairro', 'tipoLogradouro', 'nomeLogradouro')
    template_name = 'logradouro/logradouro_update_form.html'
    success_url = reverse_lazy('logradouro_list')


class LogradouroDeleteView(DeleteView):
    model = Logradouro
    template_name = 'logradouro/logradouro_delete_form.html'
    success_url = reverse_lazy('logradouro_list')
