# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 15:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_auto_20171220_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='goods_num',
            new_name='nums',
        ),
    ]
