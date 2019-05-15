from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from pessoa.models import Pessoa


class PessoaForm(forms.ModelForm):
    class Meta:
        Model = Pessoa
        fields = ('tipo_cadastro', 'nome', 'telefone', 'celular', 'email', 'ativo',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar pessoa'))
