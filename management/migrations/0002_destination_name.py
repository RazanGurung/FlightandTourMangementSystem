# Generated by Django 3.0.1 on 2020-02-04 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='Name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
