from django.db import models
# from endereco.models import endereco


# Classe pessoa
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
    tipo_cadastro = models.CharField(choices=TYPE_CAD, verbose_name=u"Tipo de Cadastro", max_length=4)
    nome = models.CharField(verbose_name=u"Nome", max_length=200)
    # endereco = models.ForeignKey(endereco, verbose_name=u"Endereço")
    telefone = models.CharField(verbose_name=u"Telefone", max_length=15)
    celular = models.CharField(verbose_name=u"Celular", max_length=15)
    email = models.EmailField(verbose_name=u"Email")
    ativo = models.BooleanField(verbose_name=u"Ativo?", blank=True)

    class Meta:
        abstract = True
