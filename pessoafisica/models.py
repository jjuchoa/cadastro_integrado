from django.db import models

from pessoa.models import Pessoa


class PessoaFisica(models.Model):
    pessoa = models.OneToOneField(Pessoa, verbose_name=u"Pessoa", on_delete=models.CASCADE, primary_key=True)
    cpf = models.CharField(verbose_name=u"CPF", max_length=15)
    rg = models.CharField(verbose_name=u"RG", max_length=15)
    dtNasc = models.DateField(verbose_name=u"Data de nascimento", auto_now_add=True)
    nomePai = models.CharField(verbose_name=u"Nome do pai", max_length=200)
    nomeMae = models.CharField(verbose_name=u"Nome da mãe", max_length=200)
    respFinanc = models.CharField(verbose_name=u"Responsável Financeiro", max_length=200)
    matricula = models.IntegerField(verbose_name=u"Matrícula")
    salario = models.CharField(verbose_name=u"Salário", max_length=100)
    comissao = models.CharField(verbose_name=u"Comissão", max_length=100)
    contratado = models.CharField(verbose_name=u"Contratado", max_length=100)
