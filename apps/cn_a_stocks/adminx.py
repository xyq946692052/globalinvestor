import xadmin
from xadmin import views

from .models import (AStocksCategory, AStocksHeader, AStocksClsePrice,
                     AStocksProfit, AStocksOperation, AStocksGrowth, AStocksBalance,
                     AStocksCashFlow, AStocksEarnRate)


class BaseSetting:
    enable_theme = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


@xadmin.sites.register(AStocksCategory)
class AStocksCategoryAdmin:
    list_display = ['id', 'category_name']
    list_filter = ['category_name']


@xadmin.sites.register(AStocksHeader)
class AStocksHeaderAdmin:
    list_filter = ['stock_name', 'stock_code']
    list_display = ['id', 'stock_name', 'stock_code', 'area']


@xadmin.sites.register(AStocksClsePrice)
class AStocksClsePriceAdmin:
    list_filter = ['stock', 'exchange_date']
    list_display = ['id', 'stock', 'exchange_date', 'closing_price']


@xadmin.sites.register(AStocksProfit)
class AStocksProfitAdmin:
    list_filter = ['stock']
    list_display = ['id', 'stock', 'pub_date', 'stat_date', 'roe_avg',
                    'np_margin', 'gp_margin', 'net_profit', 'epsttm', 'mb_revenue',
                    'total_share', 'liqa_share']


@xadmin.sites.register(AStocksOperation)
class AStocksOperationAdmin:
    list_filter = ['stock']
    list_display = ['id', 'stock', 'pub_date', 'stat_date', 'nr_turn_ratio', 'nr_turn_days',
                    'inv_turn_ratio', 'inv_turn_days', 'ca_turn_ratio', 'asset_turn_ratio']


@xadmin.sites.register(AStocksGrowth)
class AStocksGrowth:
    list_filter = ['stock']
    list_display = ['id', 'stock', 'pub_date', 'stat_date', 'yoy_equity', 'yoy_asset', 'yoy_ni',
                    'yoy_eps_basic', 'yoy_pni']


@xadmin.sites.register(AStocksBalance)
class AStocksBalanceAdmin:
    list_filter = ['stock']
    list_display = ['id', 'stock', 'pub_date', 'stat_date', 'current_ratio', 'quick_ratio',
                    'cash_ratio', 'yoy_liability', 'liability_to_asset', 'asset_to_equity']


@xadmin.sites.register(AStocksCashFlow)
class AStocksCashFlowAdmin:
    list_filter = ['stock']
    list_display = ['id', 'stock', 'pub_date', 'stat_date', 'cat_to_asset', 'nca_to_asset',
                    'tangible_asset_to_asset', 'ebit_to_interest', 'cfo_to_or', 'cfo_to_np',
                    'cfo_to_gr']


@xadmin.sites.register(AStocksEarnRate)
class AStocksEarnRateAdmin:
    list_display = ['id', 'one_month', 'three_month', 'half_year', 'one_year', 'three_year', 'five_year',
                    'ten_year']

