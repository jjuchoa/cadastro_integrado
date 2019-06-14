from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from pais.models import Pais
from estado.models import Estado
from cidade.models import Cidade
from bairro.models import Bairro
from logradouro.models import Logradouro


class EstadoForm(forms.Form):
    pais = forms.ChoiceField(choices=[(pais.pk, pais) for pais in Pais.objects.all()])
    estado = forms.ChoiceField(choices=[(estado.pk, estado) for estado in Estado.objects.all()])
    cidade = forms.ChoiceField(choices=[(cidade.pk, cidade) for cidade in Cidade.objects.all()])
    bairro = forms.ChoiceField(choices=[(bairro.pk, bairro) for bairro in Bairro.objects.all()])
    logradouro = forms.ChoiceField(choices=[(logradouro.pk, logradouro) for logradouro in Logradouro.objects.all()])
    numero = forms.IntegerField()
    cep = forms.CharField(max_length=10)

    def __init__(self, *args, **kwargs):
        super(EstadoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar Endereço'))
