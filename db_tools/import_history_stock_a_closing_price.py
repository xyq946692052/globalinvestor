import os
import sys
import csv

import baostock as bs
from time import time
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "globalinvestor.conf.test")
import django
from django.db.models import Q
django.setup()

from cn_a_stocks.models import AStocksHeader, AStocksCategory,AStocksClsePrice


def test_closing_price(stock_code, year):
    sh = AStocksHeader.objects.filter(stock_code=stock_code).first()
    scp = AStocksClsePrice.objects.filter(Q(stock_id=sh.id), Q(exchange_date__lt='2012-01-01')).all()
    for item in scp:
        print(item.exchange_date,item.closing_price)


def import_closing_price_with_file(filename):
    count = 0
    start = time()

    sh_dic = {}
    data = {}
    error_lst = []
    sh_lst = AStocksHeader.objects.all()
    for sh in sh_lst:
        sh_dic[sh.id] = sh

    with open(filename, 'r') as f:
        res = csv.reader(f)
        for exchange_date, price, stockid in res:
            if sh_dic.get(int(stockid)):
                date_ft = datetime.strptime(exchange_date, '%d/%m/%Y').strftime('%Y-%m-%d')
                data['stock'] = sh_dic.get(int(stockid))
                data['exchange_date'] = date_ft
                data['closing_price'] = price
                AStocksClsePrice.objects.create(**data)
                count += 1
                print(count, sh_dic.get(int(stockid)))
            else:
                error_lst.append(stockid)
    print('error: ', error_lst)
    print('finish, need time: {}'.format(time()-start))


def import_closing_price(start_date, end_date):
    lg = bs.login()
    shobjs = AStocksHeader.objects.all()
    count = 0
    start = time()
    print('start')
    for obj in shobjs:
        if obj.stock_code.startswith("6"):
            rs = bs.query_history_k_data_plus("sh.{}".format(obj.stock_code),
                "date, code, close, peTTM, pbMRQ, psTTM, pcfNcfTTM",
                start_date=start_date, end_date=end_date,
                frequency="d", adjustflag="3")
        else:
            rs = bs.query_history_k_data_plus("sz.{}".format(obj.stock_code),
               "date, code, close, peTTM, pbMRQ, psTTM, pcfNcfTTM",
               start_date=start_date, end_date=end_date,
               frequency="d", adjustflag="3")

        result_list = []
        while (rs.error_code == '0') & rs.next():
            result_list.append(rs.get_row_data())

        sh_lst = AStocksHeader.objects.all()
        sh_dic, data = {}, {}
        for sh in sh_lst:
            sh_dic[sh.stock_code] = sh.id

        for changedate, code, closeprice, _, _, _, _ in result_list:

            # ap = AStocksClsePrice.objects.filter(exchange_date=changedate).first()
            # if not ap:
            stock_code = code.split(".")[1]
            data['stock_id'] = sh_dic.get(stock_code)
            data['exchange_date'] = changedate
            data['closing_price'] = closeprice
            AStocksClsePrice.objects.create(**data)
        count += 1
        print('----------', count)
    print("need time: ", time()-start)
    bs.logout()


if __name__ == '__main__':
    import_closing_price('2019-12-17', '2019-12-30')
    #test_closing_price('600897', '2018')
    #import_closing_price_with_file('stocks_a_closing_price.csv')