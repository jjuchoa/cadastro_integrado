from django.db import models
from django.forms import ModelForm


class Pais(models.Model):
    codPais = models.IntegerField(verbose_name=u"Código")
    nome = models.CharField(verbose_name=u"Descrição", max_length=200)

    def __str__(self):
        return self.nome


class PaisForm(ModelForm):
    class Meta:
        Model = Pais
        fields = ('codPais', 'nome')
