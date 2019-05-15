from django.db import models
from pessoa.models import Pessoa


# Classe Pesssoa Fisica herdando da Classe pessoa
class PessoaFisica(Pessoa):
    cpf = models.CharField(verbose_name=u"CPF", max_length=15)
    rg = models.CharField(verbose_name=u"RG", max_length=15)
    dt_nasc = models.DateField(verbose_name=u"Data de nascimento", auto_now_add=True)
    nome_pai = models.CharField(verbose_name=u"Nome do pai", max_length=200)
    nome_mae = models.CharField(verbose_name=u"Nome da mãe", max_length=200)
    resp_financ = models.CharField(verbose_name=u"Responsável Financeiro", max_length=200)
    matricula = models.IntegerField(verbose_name=u"Matrícula")
    # cargo       = Tipo Cargo
    salario = models.CharField(verbose_name=u"Salário", max_length=100)
    comissao = models.CharField(verbose_name=u"Comissão", max_length=100)
    # departamento = Tipo Departamento
    contratado = models.CharField(verbose_name=u"Contratado", max_length=100)
