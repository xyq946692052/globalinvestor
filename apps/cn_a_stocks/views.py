import requests
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
    else:
        hour_price_url = 'http://image.sinajs.cn/newchart/min/n/sz{}.gif'.format(sobj.stock_code)
        daily_price_url = 'http://image.sinajs.cn/newchart/daily/n/sz{}.gif'.format(sobj.stock_code)
        week_price_url = 'http://image.sinajs.cn/newchart/weekly/n/sz{}.gif'.format(sobj.stock_code)
        month_price_url = 'http://image.sinajs.cn/newchart/monthly/n/sz{}.gif'.format(sobj.stock_code)
    view_stock_price(sobj)
    content = dict()
    content['sobj'] = sobj
    content['hour_price_url'] = hour_price_url
    content['daily_price_url'] = daily_price_url
    content['week_price_url'] = week_price_url
    content['month_price_url'] = month_price_url
    return render(request, 'cn_a_stocks/detail.html', content)




