# Generated by Django 3.2.4 on 2023-09-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kupoprodaja', '0013_auto_20230916_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='preduzece',
            name='web_site',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
