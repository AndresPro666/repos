# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0024_auto_20150930_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='CreationDate',
            field=models.DateField(default=datetime.datetime(2015, 9, 30, 6, 10, 12, 612000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='service',
            name='CreationDate',
            field=models.DateField(default=datetime.datetime(2015, 9, 30, 6, 10, 12, 597000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='service',
            name='Image',
            field=models.ImageField(default=b'/static/imagenService/foto.jpg', upload_to=b'static/ImageService'),
        ),
    ]
