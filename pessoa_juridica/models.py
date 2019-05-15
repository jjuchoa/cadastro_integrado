from django.db import models
from pessoa.models import Pessoa


# Classe pessoa Juridica herdando da Classe pessoa
class PessoaJuridica(Pessoa):
    nome_fantasia = models.CharField(verbose_name=u"Nome Fantasia", max_length=200)
    cnpj = models.CharField(verbose_name=u"CNPJ", max_length=200)
    inscEstadual = models.IntegerField(verbose_name=u"Insc. Estadual")
    # contrato = Tipo Contrato
    # socios = Tipo Socios
    # contas = Tipo Conta
    produto = models.CharField(verbose_name=u"Produto", max_length=200)
    servico = models.CharField(verbose_name=u"Serviço", max_length=200)
