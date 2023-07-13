from django.db import models

# Create your models here.
class TradeHistory(models.Model):
    bank_name = models.CharField(max_length=100)
    trading_date_time = models.DateTimeField(auto_now_add=True)
    trade_value = models.IntegerField()