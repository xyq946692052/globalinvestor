import requests
from collections import namedtuple

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render,HttpResponse

from .models import AStocksCategory, AStocksHeader
from utils import pages


def view_stock_price(objs):
    if objs.stock_code.startswith('6'):
        links = 'http://hq.sinajs.cn/list=sh{}'.format(objs.stock_code)
    else:
        links = 'http://hq.sinajs.cn/list=sz{}'.format(objs.stock_code)
    if requests.get(links).status_code == 200:
        if len(requests.get(links).text.split(',')) > 5:
            last_price, now_price = requests.get(links).text.split(',')[2:4]
            if float(last_price) != 0:
                rate_change = (float(now_price) / float(last_price) - 1) * 100
                price_change = round(rate_change, 2)
                setattr(objs, 'now_price', now_price)
                setattr(objs, 'price_change', price_change)
            else:
                setattr(objs, 'now_price', None)
                setattr(objs, 'price_change', None)


def index(request):
    name_code = request.GET.get('name_code', None)
    if name_code:
        if name_code.isdigit():
            sh_objs = AStocksHeader.objects.filter(isdelisted=False, stock_code__icontains=name_code).all()
        else:
            sh_objs = AStocksHeader.objects.filter(isdelisted=False, stock_name__icontains=name_code).all()
    else:
        sh_objs = AStocksHeader.objects.filter(isdelisted=False).all()

    context = dict()
    context['sh'], context['page_of_obj'], context['range_page'] = \
        pages.get_page_range(request, sh_objs)

    for obj in context['sh']:
        view_stock_price(obj)

    return render(request, 'cn_a_stocks/index.html', context)


def detail(request):

    stock_id = request.GET.get('sid', None)
    sobj = AStocksHeader.objects.get(pk=stock_id)

    if sobj.stock_code.startswith('6'):
        hour_price_url ='http://image.sinajs.cn/newchart/min/n/sh{}.gif'.format(sobj.stock_code)
        daily_price_url = 'http://image.sinajs.cn/newchart/daily/n/sh{}.gif'.format(sobj.stock_code)
        week_price_url = 'http://image.sinajs.cn/newchart/weekly/n/sh{}.gif'.format(sobj.stock_code)
        month_price_url = 'http://image.sinajs.cn/newchart/monthly/n/sh{}.gif'.format(sobj.stock_code)
        result = get_stock_detail_info('sh', sobj.stock_code)
    else:
        hour_price_url = 'http://image.sinajs.cn/newchart/min/n/sz{}.gif'.format(sobj.stock_code)
        daily_price_url = 'http://image.sinajs.cn/newchart/daily/n/sz{}.gif'.format(sobj.stock_code)
        week_price_url = 'http://image.sinajs.cn/newchart/weekly/n/sz{}.gif'.format(sobj.stock_code)
        month_price_url = 'http://image.sinajs.cn/newchart/monthly/n/sz{}.gif'.format(sobj.stock_code)
        result = get_stock_detail_info('sz', sobj.stock_code)
    view_stock_price(sobj)
    content = dict()
    content['sobj'] = sobj
    content['hour_price_url'] = hour_price_url
    content['daily_price_url'] = daily_price_url
    content['week_price_url'] = week_price_url
    content['month_price_url'] = month_price_url
    return render(request, 'cn_a_stocks/detail.html', content)



def get_stock_detail_info(area, stock_code):
    result = requests.get('http://sqt.gtimg.cn/q={}{}'.format(area, stock_code)).text.split('~')
    for index, k in enumerate(result):
        print(index+1,k)

    StockInfo = namedtuple('StockInfo',[
        'inx',
        'stock_name',
        'stock_code',
        'newest_price',  # 最新报价
        'closing_price',  # 昨天收盘价
        'opening_price',  # 开盘价
        'transation_num',  #成交量(万）
        'the_outer',   # 外盘
        'the_inner',   # 内盘  9
        'buy_1_price', 'buy_1_num',
        'buy_2_price', 'buy_2_num',
        'buy_3_price', 'buy_3_num',
        'buy_4_price', 'buy_4_num',
        'buy_5_price', 'buy_5_num',
        'sell_1_price', 'sell_1_num',
        'sell_2_price', 'sell_2_num',
        'sell_3_price', 'sell_3_num',
        'sell_4_price', 'sell_4_num',
        'sell_5_price', 'sell_5_num',

        'mingxi',   # 明细  30
        'nowtime',   # 当前时间
        'change_amount',  # 涨跌额(元)
        'change_price_percent',   # 涨跌幅
        'today_highest',   # 今日最高
        'today_lowest',   # 今日最低
        'close_num_price',  #收盘价/成交量/成交额
        'tradenum',  # 成交量(万手)
        'tradeprice',  # 成交额（万股）
        'turnover_rate',  # 换手率
        'pe_ttm',  # 市盈率(ttm) 40
        'unknow41',  # 未知 41
        'today_highest_1',  # 当天最高价（重复）42
        'today_lowest_1',  # 当天最低价（重复）43
        'amplitude',  # 振幅 44
        'traded_market_value',  # 流通市值(亿) 45
        'aggregate_market_value',   # 总市值(亿) 46
        'pb_ratio',   # 市净率  47
        'harden_price',  # 涨停价 48
        'drop_stop_price',   # 跌停价 49
        'quantity_relative_ratio',   # 量比 50
        'unknow51', # 51
        'average_price',  # 均价 52
        'pe_dynamic',  # 动态市盈率 53
        'pe_static_',  # 静态市盈率 54
        'unknow55',  # 55
        'unknow56',  # 56
        'unknow57',   # 57
        'tradeprice_1', #成交额(重复) 58
        'unknow59',  # 59
        'unknow60',  # 60
        'unknow61',  # 61
        'unknow62',  # 62



    ])
    # si = StockInfo(result)
    # print('==========',si.stock_name)
    return result

