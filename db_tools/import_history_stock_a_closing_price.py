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

from cn_a_stocks.models import AStocksHeader, AStocksCategory, AStocksDetail

import baostock as bs
import pandas as pd

lg = bs.login()

#### 获取沪深A股估值指标(日频)数据 ####
# peTTM    滚动市盈率
# psTTM    滚动市销率
# pcfNcfTTM    滚动市现率
# pbMRQ    市净率
rs = bs.query_history_k_data_plus("sz.000005",
    "date,code,close,peTTM,pbMRQ,psTTM,pcfNcfTTM",
    start_date='1990-12-01', end_date='2019-12-31',
    frequency="d", adjustflag="3")


#### 打印结果集 ####
result_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    result_list.append(rs.get_row_data())

for changedate, code, closeprice, _,_,_ in result_list:
    ad = AStocksDetail()

    print(changedate, code, closeprice)

#### 登出系统 ####
bs.logout()