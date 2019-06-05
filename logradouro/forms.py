from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from bairro.models import Bairro
from tipo_logradouro.models import TipoLogradouro
from nome_logradouro.models import NomeLogradouro


class LogradoroForm(forms.Form):
    bairro = forms.ChoiceField(choices=[(bairro.pk, bairro) for bairro in Bairro.objects.all()])
    tipoLogradouro = forms.ChoiceField(choices=[(tipologradouro.pk, tipologradouro) for tipologradouro in TipoLogradouro.objects.all()])
    nomeLogradouro = forms.ChoiceField(choices=[(nomelogradouro.pk, nomelogradouro) for nomelogradouro in NomeLogradouro.objects.all()])

    def __init__(self, *args, **kwargs):
        super(LogradoroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar Logradouro'))
