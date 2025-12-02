from django.db import models


# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length=122)
    middle_name = models.CharField(max_length=122)
    last_name = models.CharField(max_length=122)
    course= models.CharField(max_length=122)
    gender= models.CharField(max_length=122)
    phone= models.CharField(max_length=122)
    email = models.EmailField()
    current_address = models.TextField()
    password=models.CharField(max_length=122)
    datetime = models.DateTimeField()
