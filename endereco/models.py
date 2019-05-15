from django.db import models
# from pais.models import pais
# from estado.models import estado
# from cidade.models import cidade
# from cep.models import cep
# from bairro.models import bairro
# from logradouro.models import logradouro


# Classe endereco
class Endereco(models.Model):
    # logradouro = models.ForeignKey(logradouro, verbose_name=u"logradouro")
    # bairro = models.ForeignKey(bairro, verbose_name=u"bairro")
    numero = models.IntegerField(verbose_name=u"Número")
    # cidade = models.ForeignKey(cidade, verbose_name=u"cidade")
    # estado = models.ForeignKey(estado, verbose_name=u"EStado")
    # pais = models.ForeignKey(pais, verbose_name=u"País")
    # cep = models.ForeignKey(cep, verbose_name=u"CEP")
