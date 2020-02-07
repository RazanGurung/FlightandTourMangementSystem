# Generated by Django 3.0.1 on 2020-02-04 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('D_Id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='photo')),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Destination_Info',
            },
        ),
        migrations.CreateModel(
            name='USER',
            fields=[
                ('user_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
            ],
            options={
                'db_table': 'user_data',
            },
        ),
    ]
