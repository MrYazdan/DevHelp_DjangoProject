# Generated by Django 3.2.5 on 2021-08-23 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_user_ncode2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='lat',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='lng',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
