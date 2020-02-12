# Generated by Django 3.0.2 on 2020-01-10 20:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('ano', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2000)])),
                ('valor', models.FloatField()),
            ],
        ),
    ]
