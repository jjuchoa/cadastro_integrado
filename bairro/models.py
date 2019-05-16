from django.db import models

from cidade.models import Cidade


class Bairro(models.Model):
    cidade = models.ForeignKey(Cidade, verbose_name=u"cidade", on_delete=models.CASCADE)
    bairro = models.CharField(verbose_name=u"bairro", max_length=200)
