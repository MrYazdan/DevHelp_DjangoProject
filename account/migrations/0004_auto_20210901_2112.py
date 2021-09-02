# Generated by Django 3.2.5 on 2021-09-01 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_comment_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='writer',
        ),
        migrations.AddField(
            model_name='comment',
            name='fullname',
            field=models.CharField(default='', help_text='This is fullname of comment writer', max_length=60, verbose_name='Comment Writer Fullname'),
            preserve_default=False,
        ),
    ]