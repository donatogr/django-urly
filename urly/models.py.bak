from django.db import models

# Create your models here.
class Url(models.Model):
    short = models.CharField(_('Short url'), maxlength=255, primary=True)
    url = models.CharField(_('Original url'), maxlength=2048, db_index=True)
    