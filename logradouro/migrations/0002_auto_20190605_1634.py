# Generated by Django 2.2 on 2019-06-05 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logradouro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logradouro',
            name='bairro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bairro.Bairro', verbose_name='Bairro'),
        ),
    ]
