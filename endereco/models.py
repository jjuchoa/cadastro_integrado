from django.db import models
from django.forms import ModelForm

from pais.models import Pais
from estado.models import Estado
from cidade.models import Cidade
from bairro.models import Bairro
from logradouro.models import Logradouro


class Endereco(models.Model):
    pais = models.ForeignKey(Pais, verbose_name=u"estado", on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, verbose_name=u"estado", on_delete=models.CASCADE, null=True)
    cidade = models.ForeignKey(Cidade, verbose_name=u"cidade", on_delete=models.CASCADE, null=True)
    bairro = models.ForeignKey(Bairro, verbose_name=u"bairro", on_delete=models.CASCADE, null=True)
    logradouro = models.ForeignKey(Logradouro, verbose_name=u"logradouro", on_delete=models.CASCADE, null=True)
    numero = models.IntegerField(verbose_name=u"numero")
    cep = models.CharField(verbose_name=u"cep", max_length=10)

    def endereço(self):
        return '%s %s %s %s %s %s' % (self.logradouro, self.numero, self.bairro, self.cidade, self.estado, self.pais)


class EnderecoForm(ModelForm):
    class Meta:
        Model = Endereco
        fields = ('logradouro', 'numero', 'bairro', 'cidade', 'estado', 'pais', 'cep')
