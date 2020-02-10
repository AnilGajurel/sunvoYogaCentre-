from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password= models.CharField(max_length=60)
    class Meta:
        db_table="user"

class Customer(models.Model):
    cid = models.AutoField(auto_created=True, primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password= models.CharField(max_length=60)
    repassword= models.CharField(max_length=60)
    gender=models.CharField(max_length=20)
    bday=models.CharField(max_length=20)

    class Meta:
        db_table="customer"


class Booking(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    mobnumber=models.CharField(max_length=60)
    gender = models.CharField(max_length=100)
    classes=models.CharField(max_length=100)

    class Meta:
        db_table = "booking"


