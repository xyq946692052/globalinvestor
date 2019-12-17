from itertools import chain
from datetime import datetime
from operator import itemgetter

from django.db.models import Q

from cn_a_stocks.models import AStocksHeader, AStocksClsePrice


def get_single_earn_rate(ap_id, rank_num):

    ah = AStocksHeader.objects.get(pk=ap_id)
    if rank_num in [30, 90, 180]:
        current_year = datetime.now().year
        ap = AStocksClsePrice.objects.filter(Q(stock_id=ap_id),
            Q(exchange_date__year=current_year)).only('closing_price').values_list('closing_price').iterator()
    else:
        ap = AStocksClsePrice.objects.filter(stock_id=ap_id).only('closing_price').values_list(
            'closing_price').iterator()

    res_price = chain(*ap)
    res = [k for k in res_price]

    dt = {}
    if res and len(res) >= rank_num:
        last_price = res[-1]
        start_price = res[-rank_num]
        earn_rate = ((last_price - start_price) / start_price)*100
        dt['earn_rate'] = earn_rate
        dt['stock_id'] = ap_id
        dt['stock_code'] = ah.stock_code
        dt['stock_name'] = ah.stock_name
    else:
        dt['earn_rate'] = 0.0
        dt['stock_id'] = ap_id
        dt['stock_code'] = ah.stock_code
        dt['stock_name'] = ah.stock_name
    return dt


def get_rank_earn_rate_lst(rank_num):
    ah_ids = chain(*(AStocksHeader.objects.only('id').values_list('id').all()))
    res = []
    count = 0
    for sid in ah_ids:
        count += 1
        res.append(get_single_earn_rate(sid, rank_num))
        print(count)
    res_nearby_month = sorted(res, key=itemgetter('earn_rate'), reverse=True)
    return res_nearby_month[:20]



