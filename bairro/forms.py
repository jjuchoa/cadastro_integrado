from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from cidade.models import Cidade


class BairroForm(forms.Form):
    cidade = forms.ChoiceField(choices=[(cidade.pk, cidade) for cidade in Cidade.objects.all()])
    nome = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(BairroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar Bairro'))
