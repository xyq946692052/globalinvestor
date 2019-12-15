import os
import sys
from itertools import chain
from datetime import datetime
from django.db.models import Q

from cn_a_stocks.models import AStocksHeader, AStocksClsePrice


def get_nearmonth_rate(ap_id):
    current_year = datetime.now().year
    ah = AStocksHeader.objects.get(pk=ap_id)
    ap = AStocksClsePrice.objects.filter(Q(stock_id=ap_id), Q(exchange_date__year=current_year)).only('closing_price').values_list('closing_price')
    res_price = chain(*ap)
    res = [ k for k in res_price]
    if res and len(res) >= 30:
        last_price = res[-1]
        start_price = res[-30]
        earn_rate = round((last_price - start_price) / start_price, 4)
        dt = {}
        dt['earn_rate'] = earn_rate
        dt['stock_code'] = ah.stock_code
        return dt


