# Generated by Django 3.2.16 on 2022-12-31 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_remove_bookedsession_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedsession',
            name='time',
            field=models.IntegerField(choices=[(0, '08:00'), (1, '09:00'), (2, '10:00'), (3, '11:00'), (4, '12:00'), (5, '13:00'), (6, '14:00'), (7, '15:00'), (8, '16:00')], default=10),
            preserve_default=False,
        ),
    ]
