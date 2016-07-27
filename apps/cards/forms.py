from django import forms

class SurveyForm(forms.Form):
	cash_withdraw = forms.CharField()
	cash_swipe = forms.CharField()
	online_shopping = forms.CharField()
	flight = forms.CharField()
	car = forms.IntegerField()
	movie = forms.IntegerField()