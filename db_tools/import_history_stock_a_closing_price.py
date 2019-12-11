import os
import sys
import csv
import tushare as ts
import baostock as bs
from time import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "globalinvestor.conf.test")
import django
django.setup()

from cn_a_stocks.models import AStocksHeader, AStocksCategory,AStocksClsePrice

import baostock as bs

def import_closing_price():
    lg = bs.login()
    shobjs = AStocksHeader.objects.filter(id__gt=1000).all()
    count = 0
    start = time()
    print('start')
    for obj in shobjs:
        if obj.stock_code.startswith("6"):
            rs = bs.query_history_k_data_plus("sh.{}".format(obj.stock_code),
                "date,code,close,peTTM,pbMRQ,psTTM,pcfNcfTTM",
                start_date='2006-01-01', end_date='2019-12-31',
                frequency="d", adjustflag="3")
        else:
            rs = bs.query_history_k_data_plus("sz.{}".format(obj.stock_code),
               "date,code,close,peTTM,pbMRQ,psTTM,pcfNcfTTM",
               start_date='2006-01-01', end_date='2019-12-31',
               frequency="d", adjustflag="3")

        result_list = []
        while (rs.error_code == '0') & rs.next():
            result_list.append(rs.get_row_data())

        sh_lst = AStocksHeader.objects.all()
        sh_dic, data = {}, {}
        for sh in sh_lst:
            sh_dic[sh.stock_code] = sh.id

        for changedate, code, closeprice, _, _, _ ,_ in result_list:
            stock_code = code.split(".")[1]
            data['stock_id'] = sh_dic.get(stock_code)
            data['exchange_date'] = changedate
            data['closing_price'] = closeprice
            AStocksClsePrice.objects.create(**data)
        count += 1
        print('----------', count)
    print("need time: ",time()-start)
    bs.logout()


if __name__ == '__main__':
    import_closing_price()