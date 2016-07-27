import sys
import os

ROOT_FOLDER = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
if ROOT_FOLDER not in sys.path:
	sys.path.insert(1, ROOT_FOLDER + '/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

import django
django.setup()

from apps.cards import models
import json

f = open(os.path.abspath('./json/credit_card_data.json'), 'r')
content = f.read()
datamain = json.loads(content)

total_entries = len(datamain)
i = 0

while i < total_entries:

	models.CreditCard.objects.create(card_name = datamain[i]['Card'],
		cash_withdrawal_limit = datamain[i]['Daily cash withdrawal limit'],
		swipe_shopping_limit = datamain[i]['Daily shopping limit'],
		online_shopping_limit = datamain[i]['Daily online shopping limit'],
		reward_points = datamain[i]['Reward points on domestic transactions'],
		purchase_protection = datamain[i]['Purchase protection'],
		insurance_air = datamain[i]['Personal Accident Insurance Air'],
		insurance_non_air = datamain[i]['Personal Accident Insurance Non Air'],
		fuel_surcharge_waiver = datamain[i]['Fuel surcharge waiver'],
		emv_chip = datamain[i]['EMV card Security Chip'],
		bookmyshow = datamain[i]['Buy 1 Get 1 Free at BookMyShow.com'],
		big_cinemas = datamain[i]['Buy 1 Get 1 Free at Big Cinemas'],
		airport_lounge_access = datamain[i]['Complimentary airport lounge access'],
		joining_fee = datamain[i]['Joining Fee'],
		annual_fee = datamain[i]['Annual fee'])

	i += 1