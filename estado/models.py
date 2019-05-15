from django.db import models
# from endereco.models import endereco


# class estado(endereco):
class Estado():
    estado = models.CharField(verbose_name=u"estado", max_length=200)
