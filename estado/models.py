from django.db import models

from pais.models import Pais


class Estado(models.Model):
    pais = models.ForeignKey(Pais, verbose_name=u"pais", on_delete=models.CASCADE)
    estado = models.CharField(verbose_name=u"estado", max_length=200)
