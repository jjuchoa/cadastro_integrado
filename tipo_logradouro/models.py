from django.db import models
# from logradouro.models import logradouro


# class tipo_logradouro(logradouro):
class TipoLogradouro():
    tipoLogradouro = models.CharField(verbose_name=u"Tipo do logradouro", max_length=50)
