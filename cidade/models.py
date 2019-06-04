from django.db import models
from django.forms import ModelForm

from estado.models import Estado


class Cidade(models.Model):
    estado = models.ForeignKey(Estado, verbose_name=u"estado", on_delete=models.CASCADE)
    nome = models.CharField(verbose_name=u"cidade", max_length=200)
    numIbge = models.IntegerField(verbose_name=u"Número do IBGE")

    def __str__(self):
        return self.nome


class CidadeForm(ModelForm):
    class Meta:
        Model = Cidade
        fields = ('nome', 'numIbge', 'estado')
