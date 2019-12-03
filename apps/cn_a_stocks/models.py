from django.db import models

from datetime import datetime as dt

class AStocksCategory(models.Model):
    """所属板块"""
    category_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'stocks_a_category'


class AStocksHeader(models.Model):
    stock_name = models.CharField(max_length=20)
    category = models.ForeignKey(AStocksCategory, models.CASCADE)
    stock_code = models.CharField(max_length=10)
    area = models.CharField(max_length=10)
    ipodate = models.DateField(default=dt.now())
    outdate = models.DateField(default=dt.now())
    isdelisted = models.BooleanField(default=False)

    class Meta:
        ordering = ('stock_code', )
        db_table = 'stocks_a_header'



class AStocksDetail(models.Model):
    stock_name = models.ForeignKey(AStocksHeader, models.CASCADE)
    exchange_date = models.DateField()
    close_price = models.FloatField()

    class Meta:
        db_table = 'stocks_a_detail'
