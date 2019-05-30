from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from pessoa.models import Pessoa


class PessoaFisicaForm(forms.Form):
    nome = forms.CharField(max_length=100)
    pessoa = forms.ChoiceField(choices=[(pessoa.pk, pessoa) for pessoa in Pessoa.objects.all()])

    def __init__(self, *args, **kwargs):
        super(PessoaFisicaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar Pessoa Fisica'))
