# Generated by Django 3.2.5 on 2021-08-31 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offcode',
            name='code',
            field=models.CharField(default='9f20c83b', help_text='This is unique code for discount', max_length=80, unique=True, verbose_name='Code for discount'),
        ),
    ]
