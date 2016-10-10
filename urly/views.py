from django.shortcuts import get_object_or_404
from urly.models import Url
from django.views.generic.base import RedirectView

# Create your views here.
class Redirect(RedirectView):
	
	def get(self, path):
		short = get_object_or_404(Url, short=path).values_list('short', flat=True)[0]
		return short