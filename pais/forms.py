from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from pais.models import Pais


class PaisForm(forms.ModelForm):
    class Meta:
        Model = Pais
        fields = ('pais', 'codPais')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar pais'))
