# Generated by Django 3.2.5 on 2021-08-31 11:57

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.SlugField(default=core.utils.Controllers.Product.url_creator, help_text="This is url or link name item -> /products/'url'", unique=True, verbose_name='Link'),
        ),
    ]