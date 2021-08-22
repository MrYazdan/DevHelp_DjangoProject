# Generated by Django 3.2.5 on 2021-08-21 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_offcode_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offcode',
            name='code',
            field=models.CharField(default='fecbcbb7', help_text='This is unique code for discount', max_length=80, unique=True, verbose_name='Code for discount'),
        ),
    ]