# Generated by Django 3.2.5 on 2021-08-21 07:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_user_ncode2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ncode2',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True, validators=[django.core.validators.MaxLengthValidator(6)]),
        ),
    ]