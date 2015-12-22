# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0023_auto_20150930_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='CreationDate',
            field=models.DateField(default=datetime.datetime(2015, 9, 30, 5, 56, 41, 257000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='service',
            name='CreationDate',
            field=models.DateField(default=datetime.datetime(2015, 9, 30, 5, 56, 41, 257000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='service',
            name='Image',
            field=models.ImageField(default=b'static/imagenes/foto.jpg', upload_to=b'static/ImageService'),
        ),
    ]
