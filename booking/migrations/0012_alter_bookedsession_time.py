# Generated by Django 3.2.16 on 2022-12-30 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_auto_20221230_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedsession',
            name='time',
            field=models.IntegerField(choices=[(0, '8AM'), (1, '9AM'), (2, '10AM'), (3, '11AM'), (4, '12PM'), (5, '13PM'), (6, '14PM'), (7, '15PM'), (8, '16PM')], default=0),
        ),
    ]