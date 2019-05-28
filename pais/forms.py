from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class PaisForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PaisForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar País'))
