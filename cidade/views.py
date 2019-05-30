from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cidade.models import Cidade


class CidadeListView(ListView):
    model = Cidade
    context_object_name = 'cidade'


class CidadeCreateView(CreateView):
    model = Cidade
    fields = ('nome', 'numIbge', 'estado')
    success_url = reverse_lazy('cidade_list')


class CidadeUpdateView(UpdateView):
    model = Cidade
    fields = ('nome', 'numIbge', 'estado')
    template_name = 'cidade/cidade_update_form.html'
    success_url = reverse_lazy('cidade_list')


class CidadeDeleteView(DeleteView):
    model = Cidade
    template_name = 'cidade/cidade_delete_form.html'
    success_url = reverse_lazy('cidade_list')
