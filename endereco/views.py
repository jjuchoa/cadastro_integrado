from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from endereco.models import Endereco


class EnderecooListView(ListView):
    model = Endereco
    context_object_name = 'endereco'


class EnderecoCreateView(CreateView):
    model = Endereco
    fields = ('logradouro', 'numero', 'bairro', 'cidade', 'estado', 'pais', 'cep')
    success_url = reverse_lazy('endereco_list')


class EnderecoUpdateView(UpdateView):
    model = Endereco
    fields = ('logradouro', 'numero', 'bairro', 'cidade', 'estado', 'pais', 'cep')
    template_name = 'endereco/endereco_update_form.html'
    success_url = reverse_lazy('endereco_list')


class EnderecoDeleteView(DeleteView):
    model = Endereco
    template_name = 'endereco/endereco_delete_form.html'
    success_url = reverse_lazy('endereco_list')
