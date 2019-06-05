from django.db import models
from django.forms import ModelForm


class TipoLogradouro(models.Model):
    nome = models.CharField(verbose_name=u"Tipo do logradouro", max_length=50)

    def __str__(self):
        return self.nome


class TipoLogradouroForm(ModelForm):
    class Meta:
        Model = TipoLogradouro
        fields = ('nome',)
