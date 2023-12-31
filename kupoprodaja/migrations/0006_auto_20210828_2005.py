# Generated by Django 3.2.4 on 2021-08-28 18:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kupoprodaja', '0005_auto_20210827_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ugovor',
            name='storno',
            field=models.BooleanField(default=False, verbose_name='Stornirati:'),
        ),
        migrations.AlterField(
            model_name='ugovor',
            name='storno_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Datum storna:'),
        ),
    ]
