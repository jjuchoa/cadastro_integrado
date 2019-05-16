from django.db import models


class Cep(models.Model):
    cep = models.CharField(verbose_name=u"CEP", max_length=200)
