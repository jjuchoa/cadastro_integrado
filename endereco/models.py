from django.db import models

from pais.models import Pais
from estado.models import Estado
from cidade.models import Cidade
from cep.models import Cep
from bairro.models import Bairro
from logradouro.models import Logradouro


class Endereco(models.Model):
    pais = models.ForeignKey(Pais, verbose_name=u"estado", on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, verbose_name=u"estado", on_delete=models.CASCADE, null=True)
    cidade = models.ForeignKey(Cidade, verbose_name=u"cidade", on_delete=models.CASCADE, null=True)
    bairro = models.ForeignKey(Bairro, verbose_name=u"bairro", on_delete=models.CASCADE, null=True)
    logradouro = models.ForeignKey(Logradouro, verbose_name=u"logradouro", on_delete=models.CASCADE, null=True)
    numero = models.IntegerField(verbose_name=u"numero")
    cep = models.ForeignKey(Cep, verbose_name=u"cep", on_delete=models.CASCADE, null=True)
