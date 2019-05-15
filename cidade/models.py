from django.db import models
# from endereco.models import endereco


# class cidade(endereco):
class Cidade():
    cidade = models.CharField(verbose_name=u"cidade", max_length=200)
    numIbge = models.IntegerField(verbose_name=u"Número do IBGE", max_length=200)
