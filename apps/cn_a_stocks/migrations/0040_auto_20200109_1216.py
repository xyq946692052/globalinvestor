# Generated by Django 2.0 on 2020-01-09 04:16

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cn_a_stocks', '0039_auto_20191219_0955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='astocksbalance',
            options={'verbose_name': '偿债能力数据', 'verbose_name_plural': '偿债能力数据'},
        ),
        migrations.AlterModelOptions(
            name='astockscashflow',
            options={'verbose_name': '现金流量数据', 'verbose_name_plural': '现金流量数据'},
        ),
        migrations.AlterModelOptions(
            name='astocksclseprice',
            options={'verbose_name': '股票收盘价历史记录', 'verbose_name_plural': '股票收盘价历史记录'},
        ),
        migrations.AlterModelOptions(
            name='astocksearnrate',
            options={'verbose_name': '收益收据', 'verbose_name_plural': '收益收据'},
        ),
        migrations.AlterModelOptions(
            name='astocksgrowth',
            options={'ordering': ('stock',), 'verbose_name': '成长能力数据', 'verbose_name_plural': '成长能力数据'},
        ),
        migrations.AlterModelOptions(
            name='astocksheader',
            options={'ordering': ('stock_code',), 'verbose_name': '股票基本信息', 'verbose_name_plural': '股票基本信息'},
        ),
        migrations.AlterModelOptions(
            name='astocksoperation',
            options={'ordering': ('stock',), 'verbose_name': '营运能力数据', 'verbose_name_plural': '营运能力数据'},
        ),
        migrations.AlterModelOptions(
            name='astocksprofit',
            options={'ordering': ('stock',), 'verbose_name': '盈利能力数据', 'verbose_name_plural': '盈利能力数据'},
        ),
        migrations.AlterField(
            model_name='astocksbalance',
            name='asset_to_equity',
            field=models.FloatField(verbose_name='权益乘数'),
        ),
        migrations.AlterField(
            model_name='astocksbalance',
            name='cash_ratio',
            field=models.FloatField(verbose_name='现金比率'),
        ),
        migrations.AlterField(
            model_name='astocksbalance',
            name='current_ratio',
            field=models.FloatField(verbose_name='流动比率'),
        ),
        migrations.AlterField(
            model_name='astocksbalance',
            name='liability_to_asset',
            field=models.FloatField(verbose_name='资产负债率'),
        ),
        migrations.AlterField(
            model_name='astocksbalance',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='财报发布日'),
        ),
        migrations.AlterField(
            model_name='astocksbalance',
            name='quick_ratio',
            field=models.FloatField(verbose_name='速动比率'),
        ),
        migrations.AlterField(
            model_name='astocksbalance',
            name='stat_date',
            field=models.DateField(null=True, verbose_name='财报统计日'),
        ),
        migrations.AlterField(
            model_name='astocksbalance',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cn_a_stocks.AStocksHeader', verbose_name='股票名'),
        ),
        migrations.AlterField(
            model_name='astocksbalance',
            name='yoy_liability',
            field=models.FloatField(verbose_name='总负债同比增长率'),
        ),
        migrations.AlterField(
            model_name='astockscashflow',
            name='cat_to_asset',
            field=models.FloatField(verbose_name='流动资产占总资产比'),
        ),
        migrations.AlterField(
            model_name='astockscashflow',
            name='cfo_to_gr',
            field=models.FloatField(verbose_name='经营性现金净流量与营业总收入占比'),
        ),
        migrations.AlterField(
            model_name='astockscashflow',
            name='cfo_to_np',
            field=models.FloatField(verbose_name='经营性现金流量与总利润占比'),
        ),
        migrations.AlterField(
            model_name='astockscashflow',
            name='cfo_to_or',
            field=models.FloatField(verbose_name='营业活动产生的现金流量与营业收入占比'),
        ),
        migrations.AlterField(
            model_name='astockscashflow',
            name='ebit_to_interest',
            field=models.FloatField(verbose_name='已获利息倍数'),
        ),
        migrations.AlterField(
            model_name='astockscashflow',
            name='nca_to_asset',
            field=models.FloatField(verbose_name='非流动资产占总资产比'),
        ),
        migrations.AlterField(
            model_name='astockscashflow',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='财报发布日'),
        ),
        migrations.AlterField(
            model_name='astockscashflow',
            name='stat_date',
            field=models.DateField(null=True, verbose_name='财报发布日'),
        ),
        migrations.AlterField(
            model_name='astockscashflow',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cn_a_stocks.AStocksHeader', verbose_name='股票名'),
        ),
        migrations.AlterField(
            model_name='astockscashflow',
            name='tangible_asset_to_asset',
            field=models.FloatField(verbose_name='有形资产与总资产占比'),
        ),
        migrations.AlterField(
            model_name='astockscategory',
            name='category_name',
            field=models.CharField(max_length=50, verbose_name='板块名称'),
        ),
        migrations.AlterField(
            model_name='astocksclseprice',
            name='closing_price',
            field=models.FloatField(default=0.0, verbose_name='收盘价'),
        ),
        migrations.AlterField(
            model_name='astocksclseprice',
            name='exchange_date',
            field=models.DateField(db_index=True, null=True, verbose_name='交易日'),
        ),
        migrations.AlterField(
            model_name='astocksclseprice',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cn_a_stocks.AStocksHeader', verbose_name='股票名'),
        ),
        migrations.AlterField(
            model_name='astocksearnrate',
            name='five_year',
            field=models.TextField(verbose_name='近五年收益'),
        ),
        migrations.AlterField(
            model_name='astocksearnrate',
            name='half_year',
            field=models.TextField(verbose_name='近半年收益'),
        ),
        migrations.AlterField(
            model_name='astocksearnrate',
            name='one_month',
            field=models.TextField(verbose_name='近一个月收益'),
        ),
        migrations.AlterField(
            model_name='astocksearnrate',
            name='one_year',
            field=models.TextField(verbose_name='近一年收益'),
        ),
        migrations.AlterField(
            model_name='astocksearnrate',
            name='ten_year',
            field=models.TextField(verbose_name='近十年收益'),
        ),
        migrations.AlterField(
            model_name='astocksearnrate',
            name='three_month',
            field=models.TextField(verbose_name='近三个月收益'),
        ),
        migrations.AlterField(
            model_name='astocksearnrate',
            name='three_year',
            field=models.TextField(verbose_name='近三年收益'),
        ),
        migrations.AlterField(
            model_name='astocksgrowth',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='财报发布日'),
        ),
        migrations.AlterField(
            model_name='astocksgrowth',
            name='stat_date',
            field=models.DateField(null=True, verbose_name='财报统计日'),
        ),
        migrations.AlterField(
            model_name='astocksgrowth',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cn_a_stocks.AStocksHeader', verbose_name='股票名'),
        ),
        migrations.AlterField(
            model_name='astocksgrowth',
            name='yoy_asset',
            field=models.FloatField(verbose_name='总资产同比增长率'),
        ),
        migrations.AlterField(
            model_name='astocksgrowth',
            name='yoy_eps_basic',
            field=models.FloatField(verbose_name='基本每股收益同比增长率'),
        ),
        migrations.AlterField(
            model_name='astocksgrowth',
            name='yoy_equity',
            field=models.FloatField(verbose_name='净资产同比增长率'),
        ),
        migrations.AlterField(
            model_name='astocksgrowth',
            name='yoy_ni',
            field=models.FloatField(verbose_name='净利润同比增长率'),
        ),
        migrations.AlterField(
            model_name='astocksgrowth',
            name='yoy_pni',
            field=models.FloatField(verbose_name='归属母公司股东净利润同比增长率'),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='area',
            field=models.CharField(max_length=10, null=True, verbose_name='公司所在地'),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='business_scope',
            field=models.TextField(null=True, verbose_name='经营范围'),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cn_a_stocks.AStocksCategory', verbose_name='所属板块'),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='introduction',
            field=models.TextField(null=True, verbose_name='公司介绍'),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='ipodate',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 1, 9, 4, 16, 8, 742421, tzinfo=utc), null=True, verbose_name='上市时间'),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='isdelisted',
            field=models.BooleanField(default=False, verbose_name='是否退市'),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='main_business',
            field=models.TextField(null=True, verbose_name='主营业务'),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='outdate',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 1, 9, 4, 16, 8, 742421, tzinfo=utc), null=True, verbose_name='退市日期'),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='reg_capital',
            field=models.FloatField(default=0.0, verbose_name='注册资本'),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='stock_code',
            field=models.CharField(max_length=10, verbose_name='股票代码'),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='stock_name',
            field=models.CharField(max_length=20, verbose_name='股票名'),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='website',
            field=models.URLField(max_length=500, null=True, verbose_name='公司主页'),
        ),
        migrations.AlterField(
            model_name='astocksoperation',
            name='asset_turn_ratio',
            field=models.FloatField(verbose_name='总资产周转率'),
        ),
        migrations.AlterField(
            model_name='astocksoperation',
            name='ca_turn_ratio',
            field=models.FloatField(verbose_name='流动资产周转率'),
        ),
        migrations.AlterField(
            model_name='astocksoperation',
            name='inv_turn_days',
            field=models.FloatField(verbose_name='存货周转天数'),
        ),
        migrations.AlterField(
            model_name='astocksoperation',
            name='inv_turn_ratio',
            field=models.FloatField(verbose_name='存货周转率'),
        ),
        migrations.AlterField(
            model_name='astocksoperation',
            name='is_year_report',
            field=models.BooleanField(default=False, verbose_name='是否是年报'),
        ),
        migrations.AlterField(
            model_name='astocksoperation',
            name='nr_turn_days',
            field=models.FloatField(verbose_name='应收账款周转天数'),
        ),
        migrations.AlterField(
            model_name='astocksoperation',
            name='nr_turn_ratio',
            field=models.FloatField(verbose_name='应收账款周转率'),
        ),
        migrations.AlterField(
            model_name='astocksoperation',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='财报发布日'),
        ),
        migrations.AlterField(
            model_name='astocksoperation',
            name='stat_date',
            field=models.DateField(null=True, verbose_name='财报统计日'),
        ),
        migrations.AlterField(
            model_name='astocksoperation',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cn_a_stocks.AStocksHeader', verbose_name='股票名'),
        ),
        migrations.AlterField(
            model_name='astocksprofit',
            name='epsttm',
            field=models.FloatField(verbose_name='每股收益'),
        ),
        migrations.AlterField(
            model_name='astocksprofit',
            name='gp_margin',
            field=models.FloatField(verbose_name='销售毛利率'),
        ),
        migrations.AlterField(
            model_name='astocksprofit',
            name='is_year_report',
            field=models.BooleanField(default=False, verbose_name='是否年报'),
        ),
        migrations.AlterField(
            model_name='astocksprofit',
            name='liqa_share',
            field=models.FloatField(verbose_name='流通股本'),
        ),
        migrations.AlterField(
            model_name='astocksprofit',
            name='mb_revenue',
            field=models.FloatField(verbose_name='主营营业收入'),
        ),
        migrations.AlterField(
            model_name='astocksprofit',
            name='net_profit',
            field=models.FloatField(verbose_name='净利润'),
        ),
        migrations.AlterField(
            model_name='astocksprofit',
            name='np_margin',
            field=models.FloatField(verbose_name='销售净利率'),
        ),
        migrations.AlterField(
            model_name='astocksprofit',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='发布财报日'),
        ),
        migrations.AlterField(
            model_name='astocksprofit',
            name='roe_avg',
            field=models.FloatField(verbose_name='净资产收益率'),
        ),
        migrations.AlterField(
            model_name='astocksprofit',
            name='stat_date',
            field=models.DateField(null=True, verbose_name='财报统计季度最后一天'),
        ),
        migrations.AlterField(
            model_name='astocksprofit',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cn_a_stocks.AStocksHeader', verbose_name='股票名'),
        ),
        migrations.AlterField(
            model_name='astocksprofit',
            name='total_share',
            field=models.FloatField(verbose_name='总股本'),
        ),
    ]