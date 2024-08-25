# Generated by Django 5.1 on 2024-08-25 16:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rural_producers', '0002_alter_ruralproducers_cultivated_crops'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruralproducers',
            name='cultivated_crops',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('soja', 'Soja'), ('milho', 'Milho'), ('algodão', 'Algodão'), ('café', 'Café'), ('cana de açucar', 'Cana de açucar')], max_length=15), default=list, size=5),
        ),
    ]
