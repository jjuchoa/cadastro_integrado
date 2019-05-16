from django.db import models

from estado.models import Estado


class Cidade(models.Model):
    estado = models.ForeignKey(Estado, verbose_name=u"estado", on_delete=models.CASCADE)
    cidade = models.CharField(verbose_name=u"cidade", max_length=200)
    numIbge = models.IntegerField(verbose_name=u"Número do IBGE")
