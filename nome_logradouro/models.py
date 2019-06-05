from django.db import models
from django.forms import ModelForm


class NomeLogradouro(models.Model):
    nome = models.CharField(verbose_name=u"Nome do logradouro", max_length=50)

    def __str__(self):
        return self.nome


class NomeLogradouroForm(ModelForm):
    class Meta:
        Model = NomeLogradouro
        fields = ('nome',)
