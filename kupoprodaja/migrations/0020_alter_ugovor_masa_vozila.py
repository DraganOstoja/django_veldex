# Generated by Django 3.2.4 on 2023-09-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kupoprodaja', '0019_remove_ugovor_broker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ugovor',
            name='masa_vozila',
            field=models.CharField(max_length=20, verbose_name='Težina vozila:'),
        ),
    ]
