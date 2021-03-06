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
            name='PessoaJuridica',
            fields=[
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pessoa.Pessoa', verbose_name='Pessoa')),
                ('nomeFantasia', models.CharField(max_length=200, verbose_name='Nome Fantasia')),
                ('cnpj', models.CharField(max_length=200, verbose_name='CNPJ')),
                ('inscEstadual', models.IntegerField(verbose_name='Insc. Estadual')),
                ('produto', models.CharField(max_length=200, verbose_name='Produto')),
                ('servico', models.CharField(max_length=200, verbose_name='Serviço')),
            ],
        ),
    ]
