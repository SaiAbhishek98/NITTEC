from django.db import models


class ACL(models.Model):
    day_to_day_message = models.CharField(max_length=500)
    long_term_message = models.CharField(max_length=500)
    dates_to_remember = models.CharField(max_length=500)