from django.db import models
# from logradouro.models import logradouro


# class nome_logradouro(logradouro):
class NomeLogradouro():
    nomeLogradouro = models.CharField(verbose_name=u"Nome do logradouro", max_length=200)
