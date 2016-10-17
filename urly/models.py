from django.db import models
from django.utils.translation import ugettext_lazy as _

    
class Url(models.Model):
    short = models.CharField(_('Short url'), max_length=255, primary_key=True)
    url = models.CharField(_('Original url'), max_length=2048, db_index=True)
