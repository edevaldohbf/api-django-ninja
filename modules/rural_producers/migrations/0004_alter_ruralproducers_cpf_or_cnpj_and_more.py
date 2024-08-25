# Generated by Django 5.1 on 2024-08-25 17:02

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rural_producers', '0003_alter_ruralproducers_cultivated_crops'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruralproducers',
            name='cpf_or_cnpj',
            field=models.CharField(unique=True),
        ),
        migrations.AlterField(
            model_name='ruralproducers',
            name='cultivated_crops',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15), default=list, size=5),
        ),
    ]
