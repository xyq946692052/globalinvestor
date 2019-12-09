import os
import sys
import csv
import tushare as ts
import baostock as bs

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "globalinvestor.conf.test")
import django
django.setup()

from cn_a_stocks.models import AStocksHeader, AStocksCategory, AStocksDailyClsePrice

import baostock as bs

lg = bs.login()

shobjs = AStocksHeader.objects.all()

count = 0
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


    for changedate, code, closeprice, _,_,_,_ in result_list:
        stock_code = code.split(".")[1]
        sh = AStocksHeader.objects.filter(stock_code=stock_code).first()
        dp = AStocksDailyClsePrice()
        dp.stock = sh
        dp.exchange_date = changedate
        dp.closing_price = round(float(closeprice),2)
        dp.save()
    count += 1
    print('----------',count)

#### 登出系统 ####
bs.logout()