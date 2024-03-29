# Generated by Django 3.2.5 on 2021-08-31 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discount', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, help_text='This is active status', verbose_name='Active status')),
                ('create_time', django_jalali.db.models.jDateTimeField(auto_now_add=True, help_text='This is created time', verbose_name='Created time')),
                ('modify_time', django_jalali.db.models.jDateTimeField(auto_now=True, help_text='This is modified time', verbose_name='Modified time')),
                ('payment_datetime', django_jalali.db.models.jDateTimeField(blank=True, default=None, help_text='This is payment datetime', null=True, verbose_name='Payment Datetime')),
                ('recepie_id', models.CharField(help_text='This is recepie id for this order', max_length=64, unique=True, verbose_name='Recepie ID')),
                ('address', models.ForeignKey(blank=True, help_text='This is user address for your order', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.address', verbose_name='User address')),
                ('offcode', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='discount.offcode')),
                ('owner', models.ForeignKey(help_text='This is owner for buy cart item', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Order Owner')),
            ],
            options={
                'verbose_name': 'Order Cart',
                'verbose_name_plural': 'Order Carts',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, help_text='This is active status', verbose_name='Active status')),
                ('state_en', models.CharField(help_text='This is english order status state', max_length=90, verbose_name='English Order Status State')),
                ('state_fa', models.CharField(help_text='This is persian order status state', max_length=90, verbose_name='Persian Order Status State')),
                ('description_en', models.TextField(help_text='This is english description of product item', verbose_name='English state description')),
                ('description_fa', models.TextField(help_text='This is persian description of product item', verbose_name='Persian state description')),
            ],
            options={
                'verbose_name': 'Order Status',
                'verbose_name_plural': 'Order Statuses',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, help_text='This is active status', verbose_name='Active status')),
                ('price', models.PositiveIntegerField(help_text='This is price of this product', verbose_name='Price')),
                ('count', models.PositiveIntegerField(help_text='This is count of this product', verbose_name='Count')),
                ('order', models.ForeignKey(help_text='This is order cart', on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='Order')),
                ('product', models.ForeignKey(help_text='This is product in cart', on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'Order Items',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(help_text='This is status for paid order', on_delete=django.db.models.deletion.CASCADE, to='order.status', verbose_name='Status State'),
        ),
    ]
