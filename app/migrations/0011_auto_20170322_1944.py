# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-22 19:44
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20170322_1541'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='products',
        ),
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='basketproduct',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_products', related_query_name='basket_products', to='app.Basket'),
        ),
        migrations.AlterField(
            model_name='basketproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product'),
        ),
        migrations.AlterField(
            model_name='basketproduct',
            name='quantity',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 22, 19, 44, 29, 642738, tzinfo=utc)),
        ),
    ]
