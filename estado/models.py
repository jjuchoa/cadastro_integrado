from django.db import models
from django.forms import ModelForm

from pais.models import Pais


class Estado(models.Model):
    pais = models.ForeignKey(Pais, verbose_name=u"País", on_delete=models.CASCADE)
    nome = models.CharField(verbose_name=u"Descrição", max_length=200)

    def __str__(self):
        return self.nome


class EstadoForm(ModelForm):
    class Meta:
        Model = Estado
        fields = ('nome', 'pais')
