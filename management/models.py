from django.db import models


class USER(models.Model):
    user_id = models.AutoField(auto_created=True, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    dob = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        db_table = "user_data"


class Destination(models.Model):
    D_Id = models.AutoField(auto_created=True, primary_key=True)
    Name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/photo')
    description = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = "Destination_Info"


class Gallery(models.Model):
    G_Id = models.AutoField(auto_created=True, primary_key=True)
    Name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/photo')
    Number = models.CharField(max_length=50)

    class Meta:
        db_table = "our_gallery"
