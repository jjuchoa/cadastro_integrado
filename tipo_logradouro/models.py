from django.db import models


class TipoLogradouro(models.Model):
    tipoLogradouro = models.CharField(verbose_name=u"Tipo do logradouro", max_length=50)
