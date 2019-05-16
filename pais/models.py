from django.db import models


class Pais(models.Model):
    codPais = models.IntegerField(verbose_name=u"Código")
    pais = models.CharField(verbose_name=u"País", max_length=200)
