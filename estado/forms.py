from django import forms
from pais.models import Pais


class EstadoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    pais = forms.ChoiceField(choices=[(pais.pk, pais) for pais in Pais.objects.all()])

