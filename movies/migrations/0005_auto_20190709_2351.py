# Generated by Django 2.2.3 on 2019-07-09 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20190709_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='website',
            field=models.CharField(max_length=200),
        ),
    ]