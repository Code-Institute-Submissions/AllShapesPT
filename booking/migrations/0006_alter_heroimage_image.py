# Generated by Django 3.2.16 on 2022-12-29 14:01

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20221229_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroimage',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder_cover', max_length=255, verbose_name='image'),
        ),
    ]