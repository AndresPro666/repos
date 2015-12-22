# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0021_auto_20150927_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='CreationDate',
            field=models.DateField(default=datetime.datetime(2015, 9, 30, 5, 37, 38, 348000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='service',
            name='CreationDate',
            field=models.DateField(default=datetime.datetime(2015, 9, 30, 5, 37, 38, 348000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='service',
            name='Image',
            field=models.ImageField(default=b'imagenes/avatar.txt', upload_to=b'static/ImageService'),
        ),
        migrations.AlterField(
            model_name='service',
            name='Phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='useraql',
            name='DNI',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='useraql',
            name='Image',
            field=models.ImageField(default=b'imagenes/silueta.png', upload_to=b'static/ImageUserAQL'),
        ),
        migrations.AlterField(
            model_name='useraql',
            name='Phone',
            field=models.IntegerField(default=1),
        ),
    ]
