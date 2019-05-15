from django.db import models
# from endereco.models import endereco


# class cep(endereco):
class Cep():
    cep = models.CharField(verbose_name=u"CEP", max_length=200)
