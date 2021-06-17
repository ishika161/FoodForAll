import users
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class foodDonation:
    FOOD_TYPE = [
        ('RAW', 'Rawfood'),
        ('COOKED', 'Cookedfood'),
    ]
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None, unique=True)
    country = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    contactno = models.PositiveBigIntegerField(max_length=10)
    quantity = models.PositiveSmallIntegerField()
    food_type = models.CharField(choices=FOOD_TYPE)

class moneyDonation:
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None, unique=True)
    amount = models.PositiveBigIntegerField()
    contactno = models.PositiveBigIntegerField(max_length=10)



