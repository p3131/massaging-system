from django.db import models

# Create your models here.


class Massage(models.Model):
    sender_first_name = models.CharField(max_length=30)
    sender_last_name = models.CharField(max_length=30)
    receiver_first_name = models.CharField(max_length=30)
    receiver_last_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=100)
    massage = models.CharField(max_length=1000)
    creation_date = models.DateField()
    read_massage = models.BooleanField(default=False)