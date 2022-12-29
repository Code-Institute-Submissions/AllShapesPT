# Generated by Django 3.2.16 on 2022-12-29 13:56

import booking.models
import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20221229_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroimage',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder_cover', max_length=255,),
        ),
        migrations.AlterField(
            model_name='heroimage',
            name='slide_nr',
            field=models.IntegerField(choices=[(0, 'First'), (1, 'Second'), (2, 'Third'), (3, 'Fourth'), (4, 'Fifth')]),
        ),
    ]
