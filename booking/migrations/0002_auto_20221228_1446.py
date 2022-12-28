# Generated by Django 3.2.16 on 2022-12-28 14:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduling',
            name='special_days_off',
            field=models.TextField(help_text='Enter dates, comma separated, no space Example: 2023-01-01,2023-12-31', validators=[django.core.validators.RegexValidator('^(\\s{0,})(\\d{4}\\-\\d{2}\\-\\d{2})(,\\d{4}\\-\\d{2}\\-\\d{2}){1,}(\\s){0,}$', message='Wrong format entered!')], verbose_name='Holidays and other special days off'),
        ),
        migrations.CreateModel(
            name='BookedSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(blank=True, max_length=50, null=True)),
                ('l_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('booked_time', models.DateTimeField()),
                ('session_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='session_type', to='booking.sessiontype')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]