from django.db import models


class NomeLogradouro(models.Model):
    nomeLogradouro = models.CharField(verbose_name=u"Nome do logradouro", max_length=200)
