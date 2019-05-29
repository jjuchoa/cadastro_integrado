from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from pais.models import Pais


class EstadoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    pais = forms.ChoiceField(choices=[(pais.pk, pais) for pais in Pais.objects.all()])

    def __init__(self, *args, **kwargs):
        super(EstadoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar País'))
