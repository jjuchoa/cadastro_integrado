# Generated by Django 2.2 on 2019-05-17 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pessoa.Pessoa', verbose_name='Pessoa')),
                ('cpf', models.CharField(max_length=15, verbose_name='CPF')),
                ('rg', models.CharField(max_length=15, verbose_name='RG')),
                ('dtNasc', models.DateField(auto_now_add=True, verbose_name='Data de nascimento')),
                ('nomePai', models.CharField(max_length=200, verbose_name='Nome do pai')),
                ('nomeMae', models.CharField(max_length=200, verbose_name='Nome da mãe')),
                ('respFinanc', models.CharField(max_length=200, verbose_name='Responsável Financeiro')),
                ('matricula', models.IntegerField(verbose_name='Matrícula')),
                ('salario', models.CharField(max_length=100, verbose_name='Salário')),
                ('comissao', models.CharField(max_length=100, verbose_name='Comissão')),
                ('contratado', models.CharField(max_length=100, verbose_name='Contratado')),
            ],
        ),
    ]