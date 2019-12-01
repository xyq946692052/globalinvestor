from django.db import models

# Create your models here.

class SHHeader(models.Model):
    stock_name = models.CharField(max_length=20)
    stock_code = models.CharField(max_length=10)

    class Meta:
        db_table = 'stocks_sh_header'

class ShDetail(models.Model):
    stock_name = models.ForeignKey(SHHeader, models.CASCADE)
    exchange_date = models.DateField()
    close_price = models.FloatField()

    class Meta:
        db_table = 'stocks_sh_detail'
