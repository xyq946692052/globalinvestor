from django.db import models

from datetime import datetime as dt

class AStocksCategory(models.Model):
    """所属板块"""
    category_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'stocks_a_category'

    def __str__(self):
        return self.category_name


class AStocksHeader(models.Model):
    stock_name = models.CharField(max_length=20)  # 股票名
    category = models.ForeignKey(AStocksCategory, models.CASCADE)  # 所属板块
    stock_code = models.CharField(max_length=10) # 股票代码
    area = models.CharField(max_length=10)  # 公司所在地
    ipodate = models.DateField(default=dt.now(), null=True, blank=True) #上市时间
    outdate = models.DateField(default=dt.now(), null=True, blank=True) # 退市时间
    isdelisted = models.BooleanField(default=False)  #是否退市
    reg_capital = models.FloatField(default=0.0)  # 注册资本
    introduction = models.TextField(null=True)  # 公司介绍
    website = models.URLField(null=True, max_length=500) #公司主页
    main_business = models.TextField(null=True)  #主营业务
    business_scope = models.TextField(null=True)  #经营范围

    class Meta:
        ordering = ('stock_code', )
        db_table = 'stocks_a_header'

    def __str__(self):
        return self.stock_name


class AStocksClsePrice(models.Model):
    stock = models.ForeignKey(AStocksHeader, models.CASCADE)
    exchange_date = models.DateField(null=True)
    closing_price = models.FloatField(default=0.0)

    class Meta:
        db_table = 'stocks_a_closing_price'
