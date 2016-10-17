from django.shortcuts import get_object_or_404
from django_urly.models import Url
from django.views.generic.base import RedirectView

	
class UrlyRedirect(RedirectView):

    def get_redirect_url(self, *args, **kwargs):  # @UnusedVariable
        path = kwargs['path']
        obj = get_object_or_404(Url, short=path)
        return obj.url
