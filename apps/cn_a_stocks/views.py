import requests
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render,HttpResponse

from .models import AStocksCategory, AStocksHeader
from utils import pages


def index(request):
    name_code = request.GET.get('name_code', None)
    if name_code:
        if name_code.isdigit():
            sh_objs = AStocksHeader.objects.filter(isdelisted=False, stock_code__icontains=name_code).all()
        else:
            sh_objs = AStocksHeader.objects.filter(isdelisted=False, stock_name__icontains=name_code).all()
    else:
        sh_objs = AStocksHeader.objects.filter(isdelisted=False).all()

    context = {}
    context['sh'], context['page_of_obj'], context['range_page'] = \
        pages.get_page_range(request, sh_objs)

    view_stock_price(context['sh'])

    return render(request, 'cn_a_stocks/index.html', context)




def view_stock_price(objs):
    for obj in objs:
        if obj.stock_code.startswith('6'):
            links = 'http://hq.sinajs.cn/list=sh{}'.format(obj.stock_code)
        else:
            links = 'http://hq.sinajs.cn/list=sz{}'.format(obj.stock_code)
        if requests.get(links).status_code == 200:
            if len(requests.get(links).text.split(',')) > 5:
                last_price, now_price = requests.get(links).text.split(',')[2:4]
                if float(last_price) != 0:
                    rate_change = (float(now_price)/float(last_price)-1)*100
                    price_change = round(rate_change, 2)
                    setattr(obj, 'now_price', now_price)
                    setattr(obj, 'price_change', price_change)
                else:
                    setattr(obj, 'now_price', None)
                    setattr(obj, 'price_change', None)

