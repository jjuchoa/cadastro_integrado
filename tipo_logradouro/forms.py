from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class TipoLogradouroForm(forms.Form):
    nome = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super(TipoLogradouroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar Tipo Logradouro'))
