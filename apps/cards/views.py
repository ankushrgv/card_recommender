
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView

from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cards import models

class Index(TemplateView):

	template_name = 'cards/index.html'

	def get_context_data(self, **kwargs):

		context = super(Index, self).get_context_data(**kwargs)
		return context

class CardList(ListView):

	model = models.CreditCard
	template = 'cards/card_list.html'

	def get_score(self, a, b, lookup_value):

		cash_withdraw_lookup = [50000, 100000, 150000, 200000, 250000]
		card_swipe_lookup = [100000, 150000, 200000, 250000, 300000]
		online_shopping_lookup = [100000, 150000, 200000, 250000, 300000]

		if lookup_value == 1:
			lookup = cash_withdraw_lookup
		elif lookup_value == 2:
			lookup = card_swipe_lookup
		else:
			lookup = online_shopping_lookup

		user_demand = lookup[int(a)]
		card_value = b

		difference = card_value - user_demand

		if difference == 0:
			difference = 1
			

		if difference < 0:
			numerator = difference
			denominator = user_demand

		else:
			numerator = user_demand
			if difference == 1:
				denominator = lookup[4]
			else:
				denominator = difference

		score = ((float(numerator) * 10) / (float(denominator)))

		# print " score = ", score
		return score

	def post(self, request):

		if request.method == 'POST':

			context = request.POST
			card_scores = {}

			credit_cards = models.CreditCard.objects.all()

			for card in credit_cards:

				print "card = ", card.card_name

				cash_withdraw_score = self.get_score(context['cash_withdraw'], card.cash_withdrawal_limit, 1)
				card_swipe_score = self.get_score(context['cash_swipe'], card.swipe_shopping_limit, 2)
				online_shopping_score = self.get_score(context['online_shopping'], card.online_shopping_limit, 3)

				print "first three = ", (cash_withdraw_score + card_swipe_score + online_shopping_score)
				
				reward_point_score = float(card.reward_points) / 10.00 
				# print "rp score = ", reward_point_score
				
				purchase_protection_score = float(card.purchase_protection) / 500000.00
				# print "pp_score = ", purchase_protection_score
				
				air_allowances_score = (float(context['flight']) ** float(context['flight'])) * ((float(card.insurance_air) / 30000000.00) + (float(card.airport_lounge_access) / 4.00))
				# print "air_allowances_score = ", air_allowances_score

				non_air_allowances_score = (float(context['car']) ** float(context['car'])) * ((float(card.insurance_non_air) / 30000000.00) + (float(card.fuel_surcharge_waiver)))
				# print "non_air_allowances_score = ", non_air_allowances_score				

				emv_score = float(card.emv_chip)
				# print "emv score = ", emv_score

				bookmyshow_score = float(card.emv_chip)
				# print "bms score = ", bookmyshow_score

				big_cinemas_score = float(card.emv_chip)
				# print "bigcen score = ", big_cinemas_score

				if card.joining_fee == 0:
					card_joining_fee = 100.00
				else:
					card_joining_fee = float(card.joining_fee)

				joining_fee_score = (100.00) / card_joining_fee 

				annual_fee_score = (100.00) / card.annual_fee

				card_scores[card.id] = cash_withdraw_score + card_swipe_score + online_shopping_score + reward_point_score \
				+ purchase_protection_score + air_allowances_score + non_air_allowances_score + emv_score + bookmyshow_score \
				+ big_cinemas_score + joining_fee_score + annual_fee_score

				# print "total score = ", card_scores[card.id]

			print card_scores
