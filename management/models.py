from django.db import models


class User(models.Model):
    user_id = models.AutoField(auto_created=True, primary_key=True)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Gender=models.CharField(max_length=10)
    class Meta:
        db_table = "user"
