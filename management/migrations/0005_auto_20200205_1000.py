# Generated by Django 3.0.1 on 2020-02-05 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20200205_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='destination',
            name='price',
            field=models.IntegerField(max_length=5),
        ),
    ]