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
    category = models.ForeignKey(AStocksCategory, models.CASCADE, null=True)  # 所属板块
    stock_code = models.CharField(max_length=10) # 股票代码
    area = models.CharField(max_length=10, null=True)  # 公司所在地
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
    exchange_date = models.DateField(null=True)  #交易日
    closing_price = models.FloatField(default=0.0)  #收盘价

    class Meta:
        db_table = 'stocks_a_closing_price'


# 盈利数据
class AStocksProfit(models.Model):
    stock = models.ForeignKey(AStocksHeader, models.CASCADE)
    pub_date = models.DateField(null=True)  #公司发布财报的日期
    stat_date = models.DateField(null=True)  # 财报统计的季度最后一天
    roe_avg = models.FloatField()  #净资产收益率(平均)%
    np_margin = models.FloatField()  # 销售净利率（%）
    gp_margin = models.FloatField()  # 销售毛利率（%）
    net_profit = models.FloatField()  # 净利润(元）
    epsttm = models.FloatField()  # 每股收益
    mb_revenue = models.FloatField()  # 主营营业收入（元）
    total_share = models.FloatField()  # 总股本
    liqa_share = models.FloatField()  # 流通股本
    is_year_report = models.BooleanField(default=False)  # 是否是年报

    class Meta:
        db_table = 'stocks_a_profile'


# 营运能力数据
class AStocksOperation(models.Model):
    stock = models.ForeignKey(AStocksHeader, models.CASCADE)
    pub_date = models.DateField(null=True)  # 公司发布财报的日期
    stat_date = models.DateField(null=True)  # 财报统计的季度的最后一天
    nr_turn_ratio = models.FloatField()   # 应收账款周转率(次)
    nr_turn_days = models.FloatField()   # 应收账款周转天数(天)
    inv_turn_ratio = models.FloatField()  # 存货周转率(次)
    inv_turn_days = models.FloatField()   # 存货周转天数(天)
    ca_turn_ratio = models.FloatField()   # 流动资产周转率(次)
    asset_turn_ratio = models.FloatField()  # 总资产周转率
    is_year_report = models.BooleanField(default=False) # 是否是年报

    class Meta:
        db_table = 'stocks_a_operation'


# 成长能力
class AStocksGrowth(models.Model):
    stock = models.ForeignKey(AStocksHeader, models.CASCADE)
    pub_date = models.DateField(null=True)  # 公司发布财报的日期
    stat_date = models.DateField(null=True)  # 财报统计的季度的最后一天
    yoy_equity = models.FloatField()  # 净资产同比增长率
    yoy_asset = models.FloatField()  # 总资产同比增长率
    yoy_ni = models.FloatField()  # 净利润同比增长率
    yoy_eps_basic = models.FloatField()  # 基本每股收益同比增长率
    yoy_pni = models.FloatField()  # 归属母公司股东净利润同比增长率

    class Meta:
        db_table = 'stocks_a_growth'


# 偿债能力
class AStocksBalance(models.Model):
    stock = models.ForeignKey(AStocksHeader, models.CASCADE)
    pub_date = models.DateField(null=True)  # 公司发布财报的日期
    stat_date = models.DateField(null=True)  # 财报统计的季度的最后一天
    current_ratio = models.FloatField()  # 流动比率
    quick_ratio = models.FloatField()  # 速动比率
    cash_ratio = models.FloatField()  # 现金比率
    yoy_liability = models.FloatField()  # 总负债同比增长率
    liability_to_asset = models.FloatField()  # 资产负债率
    asset_to_equity = models.FloatField()  # 权益乘数

    class Meta:
        db_table = 'stocks_a_balance'


#现金流量
class AStocksCashFlow(models.Model):
    stock = models.ForeignKey(AStocksHeader, models.CASCADE)
    pub_date = models.DateField(null=True)  # 公司发布财报的日期
    stat_date = models.DateField(null=True)  # 财报统计的季度的最后一天
    cat_to_asset = models.FloatField()  # 流动资产除以总资产
    nca_to_asset = models.FloatField()  # 非流动资产除以总资产
    tangible_asset_to_asset = models.FloatField()   # 有形资产除以总资产
    ebit_to_interest = models.FloatField()  # 已获利息倍数
    cfo_to_or = models.FloatField()   # 经营活动产生的现金流量净额除以营业收入
    cfo_to_np = models.FloatField()   # 经营性现金净流量除以净利润
    cfo_to_gr = models.FloatField()   # 经营性现金净流量除以营业总收入

    class Meta:
        db_table = 'stocks_a_cashflow'








