# Generated by Django 3.2.5 on 2021-08-17 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_user_ncode'),
        ('order', '0002_auto_20210815_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(blank=True, help_text='This is user address for your order', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.address', verbose_name='User address'),
        ),
    ]
