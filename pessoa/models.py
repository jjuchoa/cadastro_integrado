from django.db import models

from endereco.models import Endereco


class Pessoa(models.Model):
    FORNECEDOR = "forn"
    CLIENTE = "clie"
    TERCEIRIZADO = "terc"
    FUNCIONARIO = "func"

    TYPE_CAD = (
        (FORNECEDOR, "Fornecedor"),
        (CLIENTE, "Cliente"),
        (TERCEIRIZADO, "Terceirizado"),
        (FUNCIONARIO, "Funcionário"),
    )

    # ESCOLHAS
    endereco = models.ForeignKey(Endereco, verbose_name=u"Endereço", on_delete=models.CASCADE)
    tipoCadastro = models.CharField(choices=TYPE_CAD, verbose_name=u"Tipo de Cadastro", max_length=4)
    nome = models.CharField(verbose_name=u"Nome", max_length=200)
    telefone = models.CharField(verbose_name=u"Telefone", max_length=15)
    celular = models.CharField(verbose_name=u"Celular", max_length=15)
    email = models.EmailField(verbose_name=u"Email")
    ativo = models.BooleanField(verbose_name=u"Ativo?", blank=True)
