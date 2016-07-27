from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CreditCard(models.Model):
	card_name = models.CharField(max_length=40)
	cash_withdrawal_limit = models.PositiveIntegerField()
	swipe_shopping_limit = models.PositiveIntegerField()
	online_shopping_limit = models.PositiveIntegerField()
	reward_points = models.PositiveSmallIntegerField()
	purchase_protection = models.PositiveIntegerField()
	insurance_air = models.PositiveIntegerField()
	insurance_non_air = models.PositiveIntegerField()
	fuel_surcharge_waiver = models.BooleanField(default=False)
	emv_chip = models.BooleanField(default=False)
	bookmyshow = models.BooleanField(default=False)
	big_cinemas = models.BooleanField(default=False)
	airport_lounge_access = models.PositiveIntegerField()		
	joining_fee = models.PositiveIntegerField()
	annual_fee = models.PositiveIntegerField()