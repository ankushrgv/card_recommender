
from django.views.generic.base import TemplateView
# Create your views here.

class Index(TemplateView):

	template_name = 'cards/index.html'

	def get_context_data(self, **kwargs):

		context = super(Index, self).get_context_data(**kwargs)
		return context

