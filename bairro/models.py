from django.db import models
from django.forms import ModelForm

from cidade.models import Cidade


class Bairro(models.Model):
    cidade = models.ForeignKey(Cidade, verbose_name=u"cidade", on_delete=models.CASCADE)
    nome = models.CharField(verbose_name=u"bairro", max_length=200)

    def __str__(self):
        return self.nome


class BairroForm(ModelForm):
    class Meta:
        Model = Bairro
        fields = ('nome', 'cidade')
