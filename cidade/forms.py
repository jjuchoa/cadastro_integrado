from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from estado.models import Estado


class CidadeForm(forms.Form):
    estado = forms.ChoiceField(choices=[(estado.pk, estado) for estado in Estado.objects.all()])
    nome = forms.CharField(max_length=100)
    numIbge = forms.IntegerField

    def __init__(self, *args, **kwargs):
        super(CidadeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar Cidade'))
