from django.db import models
from django.forms import ModelForm

from bairro.models import Bairro
from tipo_logradouro.models import TipoLogradouro
from nome_logradouro.models import NomeLogradouro


class Logradouro(models.Model):
    bairro = models.ForeignKey(Bairro, verbose_name=u"Bairro", on_delete=models.CASCADE)
    tipoLogradouro = models.ForeignKey(TipoLogradouro, verbose_name=u"Tipo de logradouro", on_delete=models.CASCADE)
    nomeLogradouro = models.ForeignKey(NomeLogradouro, verbose_name=u"Nome do logradouro", on_delete=models.CASCADE)

    def logradouro(self):
        return '%s %s' % (self.tipoLogradouro, self.nomeLogradouro)



class EstadoForm(ModelForm):
    class Meta:
        Model = Logradouro
        fields = ('bairro', 'tipoLogradouro', 'nomeLogradouro')
