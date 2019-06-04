from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from bairro.models import Bairro


class BairroListView(ListView):
    model = Bairro
    context_object_name = 'bairro'


class BairroCreateView(CreateView):
    model = Bairro
    fields = ('nome', 'cidade')
    success_url = reverse_lazy('bairro_list')


class BairroUpdateView(UpdateView):
    model = Bairro
    fields = ('nome', 'cidade')
    template_name = 'bairro/bairro_update_form.html'
    success_url = reverse_lazy('bairro_list')


class BairroDeleteView(DeleteView):
    model = Bairro
    template_name = 'bairro/bairro_delete_form.html'
    success_url = reverse_lazy('bairro_list')
