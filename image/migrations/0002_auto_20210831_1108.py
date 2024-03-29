# Generated by Django 3.2.5 on 2021-08-31 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
        migrations.AlterModelOptions(
            name='multiimages',
            options={'verbose_name': 'Image Album', 'verbose_name_plural': 'Albums'},
        ),
        migrations.AddField(
            model_name='multiimages',
            name='name',
            field=models.CharField(default='test album', help_text='This is album name (for hint to select true album)', max_length=60, verbose_name='Album Name'),
            preserve_default=False,
        ),
    ]
