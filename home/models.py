import users
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class foodDonation(models.Model):
    FOOD_TYPE = [
        ('RAW', 'Rawfood'),
        ('COOKED', 'Cookedfood'),
    ]
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    country = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    contactno = models.PositiveBigIntegerField()
    quantity = models.PositiveSmallIntegerField()
    food_type = models.CharField(choices=FOOD_TYPE, max_length=10)

class moneyDonation(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    amount = models.PositiveBigIntegerField()
    contactno = models.PositiveBigIntegerField()

class contact(models.Model):
    name = models.CharField(max_length=30)
    sender_email = models.EmailField(max_length=30)
    body = models.CharField(max_length=300)
    



