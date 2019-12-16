import os
import sys
import json
from datetime import datetime as dt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "globalinvestor.conf.test")
import django
from django.db.models import Q
django.setup()

from cn_a_stocks.models import AStocksHeader, AStocksEarnRate
from utils.get_yield_rate import get_rank_earn_rate_lst


def update_all():
    current = dt.now()

    ae = AStocksEarnRate.objects.filter(Q(update_date__year=current.year),
                                        Q(update_date__month=current.month)).first()
    if ae:
        ae.one_month = json.dumps(get_rank_earn_rate_lst(30))
        ae.three_month = json.dumps(get_rank_earn_rate_lst(90))
        ae.half_year = json.dumps(get_rank_earn_rate_lst(180))
        ae.one_year = json.dumps(get_rank_earn_rate_lst(360))
        ae.three_year = json.dumps(get_rank_earn_rate_lst(1080))
        ae.five_year = json.dumps(get_rank_earn_rate_lst(1800))
        ae.ten_year = json.dumps(get_rank_earn_rate_lst(3600))
        ae.save()
    else:
        params = {}
        params['one_month'] = json.dumps(get_rank_earn_rate_lst(30))
        params['three_month'] = json.dumps(get_rank_earn_rate_lst(90))
        params['half_year'] = json.dumps(get_rank_earn_rate_lst(180))
        params['one_year'] = json.dumps(get_rank_earn_rate_lst(360))
        params['three_year'] = json.dumps(get_rank_earn_rate_lst(1080))
        params['five_year'] = json.dumps(get_rank_earn_rate_lst(1800))
        params['ten_year'] = json.dumps(get_rank_earn_rate_lst(3600))
        AStocksEarnRate.objects.create(**params)
    print('finish update...')


def update_single(rank_type, rank_num):
    current = dt.now()
    ae = AStocksEarnRate.objects.filter(Q(update_date__year=current.year),
                                        Q(update_date__month=current.month)).first()
    res = json.dumps(get_rank_earn_rate_lst(rank_num))
    setattr(ae, rank_type, res)
    print('update {} finishing...'.format(rank_type))


if __name__ == '__main__':
    update_single('one_year', 360)



