# Generated by Django 3.2.5 on 2021-08-17 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_offcode_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offcode',
            name='code',
            field=models.CharField(default='598b8c94', help_text='This is unique code for discount', max_length=80, unique=True, verbose_name='Code for discount'),
        ),
    ]
