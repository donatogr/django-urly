from django.db import models

# Create your models here.
class Url(models.Model):
	short = models.CharField(_('Short url'), maxlength=255, unique=True)
	url = models.CharField(_('Original url'), maxlength=2048, unique=True)
	