from django.db import models
# from endereco.models import endereco


# class bairro(endereco):
class Bairro():
    bairro = models.CharField(verbose_name=u"bairro", max_length=200)
