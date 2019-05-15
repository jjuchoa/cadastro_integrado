from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from pessoa.models import Pessoa
from pessoa.forms import PessoaForm


class PessoaListView(ListView):
    model = Pessoa
    context_object_name = 'pessoa'


class PessoaCreateView(CreateView):
    model = Pessoa
    fields = 'nome'
    success_url = reverse_lazy('pessoa_list')


class PersonUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    # template_name = 'pessoa/pais_update_form.html'
    success_url = reverse_lazy('pessoa_list')
