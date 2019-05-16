from django.db import models

from pessoa.models import Pessoa


class PessoaJuridica(models.Model):
    pessoa = models.OneToOneField(Pessoa, verbose_name=u"Pessoa", on_delete=models.CASCADE, primary_key=True)
    nomeFantasia = models.CharField(verbose_name=u"Nome Fantasia", max_length=200)
    cnpj = models.CharField(verbose_name=u"CNPJ", max_length=200)
    inscEstadual = models.IntegerField(verbose_name=u"Insc. Estadual")
    produto = models.CharField(verbose_name=u"Produto", max_length=200)
    servico = models.CharField(verbose_name=u"Serviço", max_length=200)
