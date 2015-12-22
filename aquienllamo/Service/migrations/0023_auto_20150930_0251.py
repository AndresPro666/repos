# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0022_auto_20150930_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='CreationDate',
            field=models.DateField(default=datetime.datetime(2015, 9, 30, 5, 51, 36, 964000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='service',
            name='CreationDate',
            field=models.DateField(default=datetime.datetime(2015, 9, 30, 5, 51, 36, 964000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='service',
            name='Image',
            field=models.ImageField(default=b'static/imagenes/avatar.txt', upload_to=b'static/ImageService'),
        ),
        migrations.AlterField(
            model_name='service',
            name='NameService',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='useraql',
            name='Image',
            field=models.ImageField(default=b'static/imagenes/silueta.png', upload_to=b'static/ImageUserAQL'),
        ),
    ]
