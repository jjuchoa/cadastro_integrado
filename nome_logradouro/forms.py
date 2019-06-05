from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class NomeLogradouroForm(forms.Form):
    nome = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super(NomeLogradouroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar Nome Logradouro'))
