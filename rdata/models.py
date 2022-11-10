
from django.conf import settings
from django.db import models
from django.utils.timezone import now


# Create your models here.


class Csv(models.Model):
    csv_file = models.TextField()


class TradingData(models.Model):
    Date = models.DateTimeField(default=now, blank=True)
    Open = models.CharField(max_length=100, blank=True)
    Close = models.CharField(max_length=100, blank=True)
    High = models.CharField(max_length=100, blank=True)
    Low = models.CharField(max_length=100, blank=True)
    Adj_Close = models.CharField(max_length=100, blank=True)
    Volume = models.CharField(max_length=100, blank=True)
