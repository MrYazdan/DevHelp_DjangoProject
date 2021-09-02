# Generated by Django 3.2.5 on 2021-08-31 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(help_text='This is product for set comment for this', on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(blank=True, help_text='This is reply for this commnet', null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.comment', verbose_name='Reply'),
        ),
        migrations.AddField(
            model_name='comment',
            name='writer',
            field=models.ForeignKey(help_text='This is comment writer', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Comment Writer'),
        ),
    ]