from django.db import models

from django.utils import timezone
from django.utils.timezone import now


class AStocksCategory(models.Model):
    """所属板块"""
    category_name = models.CharField(max_length=50, verbose_name='板块名称')

    class Meta:
        verbose_name = verbose_name_plural = '板块'
        ordering = ('category_name', )
        db_table = 'stocks_a_category'

    def __str__(self):
        return self.category_name


class AStocksHeader(models.Model):
    """股票基本信息"""
    stock_name = models.CharField(max_length=20, verbose_name='股票名')  # 股票名
    category = models.ForeignKey(AStocksCategory, models.CASCADE, null=True, verbose_name='所属板块')  # 所属板块
    stock_code = models.CharField(max_length=10, verbose_name='股票代码')  # 股票代码
    area = models.CharField(max_length=10, null=True, verbose_name='公司所在地')  # 公司所在地
    #ipodate = models.DateField(default=now(), null=True, blank=True, verbose_name='上市时间')  # 上市时间
    #outdate = models.DateField(default=now(), null=True, blank=True, verbose_name='退市日期')  # 退市时间
    isdelisted = models.BooleanField(default=False, verbose_name='是否退市')   # 是否退市
    reg_capital = models.FloatField(default=0.0, verbose_name='注册资本')  # 注册资本
    introduction = models.TextField(null=True, verbose_name='公司介绍')  # 公司介绍
    website = models.URLField(null=True, max_length=500, verbose_name='公司主页')  # 公司主页
    main_business = models.TextField(null=True, verbose_name='主营业务')   # 主营业务
    business_scope = models.TextField(null=True, verbose_name='经营范围')   # 经营范围

    class Meta:
        ordering = ('stock_code', )
        db_table = 'stocks_a_header'
        verbose_name = verbose_name_plural = '股票基本信息'

    def __str__(self):
        return self.stock_name


class AStocksClsePrice(models.Model):
    """股票收盘价信息"""
    stock = models.ForeignKey(AStocksHeader, models.CASCADE, verbose_name='股票名')
    exchange_date = models.DateField(null=True, db_index=True, verbose_name='交易日')  # 交易日
    closing_price = models.FloatField(default=0.0, verbose_name='收盘价')  # 收盘价

    class Meta:
        db_table = 'stocks_a_closing_price'
        verbose_name = verbose_name_plural = '股票收盘价历史记录'


class AStocksProfit(models.Model):
    """盈利能力"""
    stock = models.ForeignKey(AStocksHeader, models.CASCADE, verbose_name='股票名')
    pub_date = models.DateField(null=True, verbose_name='发布财报日')  # 公司发布财报的日期
    stat_date = models.DateField(null=True, verbose_name='财报统计季度最后一天')  # 财报统计的季度最后一天
    roe_avg = models.FloatField(verbose_name='净资产收益率')  # 净资产收益率(平均)%
    np_margin = models.FloatField(verbose_name='销售净利率')  # 销售净利率（%）
    gp_margin = models.FloatField(verbose_name='销售毛利率')  # 销售毛利率（%）
    net_profit = models.FloatField(verbose_name='净利润')  # 净利润(元）
    epsttm = models.FloatField(verbose_name='每股收益')  # 每股收益
    mb_revenue = models.FloatField(verbose_name='主营营业收入')  # 主营营业收入（元）
    total_share = models.FloatField(verbose_name='总股本')  # 总股本
    liqa_share = models.FloatField(verbose_name='流通股本')  # 流通股本
    is_year_report = models.BooleanField(default=False, verbose_name='是否年报')  # 是否是年报

    class Meta:
        db_table = 'stocks_a_profile'
        ordering = ('stock',)
        verbose_name = verbose_name_plural = '盈利能力数据'


class AStocksOperation(models.Model):
    """营运能力"""
    stock = models.ForeignKey(AStocksHeader, models.CASCADE, verbose_name='股票名')
    pub_date = models.DateField(null=True, verbose_name='财报发布日')  # 公司发布财报的日期
    stat_date = models.DateField(null=True, verbose_name='财报统计日')  # 财报统计的季度的最后一天
    nr_turn_ratio = models.FloatField(verbose_name='应收账款周转率')   # 应收账款周转率(次)
    nr_turn_days = models.FloatField(verbose_name='应收账款周转天数')   # 应收账款周转天数(天)
    inv_turn_ratio = models.FloatField(verbose_name='存货周转率')  # 存货周转率(次)
    inv_turn_days = models.FloatField(verbose_name='存货周转天数')   # 存货周转天数(天)
    ca_turn_ratio = models.FloatField(verbose_name='流动资产周转率')   # 流动资产周转率(次)
    asset_turn_ratio = models.FloatField(verbose_name='总资产周转率')  # 总资产周转率
    is_year_report = models.BooleanField(default=False, verbose_name='是否是年报')  # 是否是年报

    class Meta:
        db_table = 'stocks_a_operation'
        ordering = ('stock', )
        verbose_name = verbose_name_plural = '营运能力数据'


class AStocksGrowth(models.Model):
    """成长能力"""
    stock = models.ForeignKey(AStocksHeader, models.CASCADE, verbose_name='股票名')
    pub_date = models.DateField(null=True, verbose_name='财报发布日')  # 公司发布财报的日期
    stat_date = models.DateField(null=True, verbose_name='财报统计日')  # 财报统计的季度的最后一天
    yoy_equity = models.FloatField(verbose_name='净资产同比增长率')  # 净资产同比增长率
    yoy_asset = models.FloatField(verbose_name='总资产同比增长率')  # 总资产同比增长率
    yoy_ni = models.FloatField(verbose_name='净利润同比增长率')  # 净利润同比增长率
    yoy_eps_basic = models.FloatField(verbose_name='基本每股收益同比增长率')  # 基本每股收益同比增长率
    yoy_pni = models.FloatField(verbose_name='归属母公司股东净利润同比增长率')  # 归属母公司股东净利润同比增长率

    class Meta:
        db_table = 'stocks_a_growth'
        ordering = ('stock', )
        verbose_name = verbose_name_plural = '成长能力数据'


class AStocksBalance(models.Model):
    """偿债能力"""
    stock = models.ForeignKey(AStocksHeader, models.CASCADE, verbose_name='股票名')
    pub_date = models.DateField(null=True, verbose_name='财报发布日')  # 公司发布财报的日期
    stat_date = models.DateField(null=True, verbose_name='财报统计日')  # 财报统计的季度的最后一天
    current_ratio = models.FloatField(verbose_name='流动比率')  # 流动比率
    quick_ratio = models.FloatField(verbose_name='速动比率')  # 速动比率
    cash_ratio = models.FloatField(verbose_name='现金比率')  # 现金比率
    yoy_liability = models.FloatField(verbose_name='总负债同比增长率')  # 总负债同比增长率
    liability_to_asset = models.FloatField(verbose_name='资产负债率')  # 资产负债率
    asset_to_equity = models.FloatField(verbose_name='权益乘数')  # 权益乘数

    class Meta:
        db_table = 'stocks_a_balance'
        verbose_name = verbose_name_plural = '偿债能力数据'


class AStocksCashFlow(models.Model):
    """现金流量"""
    stock = models.ForeignKey(AStocksHeader, models.CASCADE, verbose_name='股票名')
    pub_date = models.DateField(null=True, verbose_name='财报发布日')  # 公司发布财报的日期
    stat_date = models.DateField(null=True, verbose_name='财报发布日')  # 财报统计的季度的最后一天
    cat_to_asset = models.FloatField(verbose_name='流动资产占总资产比')  # 流动资产除以总资产
    nca_to_asset = models.FloatField(verbose_name='非流动资产占总资产比')  # 非流动资产除以总资产
    tangible_asset_to_asset = models.FloatField(verbose_name='有形资产与总资产占比')   # 有形资产除以总资产
    ebit_to_interest = models.FloatField(verbose_name='已获利息倍数')  # 已获利息倍数
    cfo_to_or = models.FloatField(verbose_name='营业活动产生的现金流量与营业收入占比')   # 经营活动产生的现金流量净额除以营业收入
    cfo_to_np = models.FloatField(verbose_name='经营性现金流量与总利润占比')   # 经营性现金净流量除以净利润
    cfo_to_gr = models.FloatField(verbose_name='经营性现金净流量与营业总收入占比')   # 经营性现金净流量除以营业总收入

    class Meta:
        db_table = 'stocks_a_cashflow'
        verbose_name = verbose_name_plural = '现金流量数据'


class AStocksEarnRate(models.Model):
    """收益率数据"""
    one_month = models.TextField(verbose_name='近一个月收益')
    three_month = models.TextField(verbose_name='近三个月收益')
    half_year = models.TextField(verbose_name='近半年收益')
    one_year = models.TextField(verbose_name='近一年收益')
    three_year = models.TextField(verbose_name='近三年收益')
    five_year = models.TextField(verbose_name='近五年收益')
    ten_year = models.TextField(verbose_name='近十年收益')
    create_date = models.DateField(auto_now_add=timezone.now())
    update_date = models.DateField(auto_now=timezone.now())

    class Meta:
        db_table = 'stocks_a_earnrate'
        verbose_name = verbose_name_plural = '收益收据'



