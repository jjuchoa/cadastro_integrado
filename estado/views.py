from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from estado.models import Estado
from estado.forms import EstadoForm


class EstadoListView(ListView):
    model = Estado
    context_object_name = 'estado'


class EstadoCreateView(CreateView):
    model = Estado
    fields = ('nome', 'pais')
    success_url = reverse_lazy('estado_list')


class EstadoUpdateView(UpdateView):
    model = Estado
    form_class = EstadoForm
    template_name = 'estado/estado_update_form.html'
    success_url = reverse_lazy('estado_list')
