from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from pais.models import Pais
from pais.forms import PaisForm


class PaisListView(ListView):
    model = Pais
    context_object_name = 'pais'


class PaisCreateView(CreateView):
    model = Pais
    fields = ('codPais', 'nome')
    success_url = reverse_lazy('pais_list')


class PaisUpdateView(UpdateView):
    model = Pais
    form_class = PaisForm
    template_name = 'pais/pais_update_form.html'
    success_url = reverse_lazy('pais_list')
