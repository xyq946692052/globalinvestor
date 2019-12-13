import os
import sys
import baostock as bs
import pandas as pd
from time import time


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "globalinvestor.conf.test")
import django
django.setup()

from cn_a_stocks.models import AStocksHeader, AStocksBalance

def query_balance():
    # 接口提供的数据最早从2007年开始
    lg = bs.login()
    shobjs = AStocksHeader.objects.all()
    count = 0
    start = time()
    error_code = []
    for obj in shobjs:
        # 如果数据库中已有该股票的记录，则跳过此股票继续循环
        if AStocksBalance.objects.filter(stock=obj):
            print("exist: ", obj.stock_code)
            continue

        try:
            balance_list = []
            count += 1
            print(count)
            for year in range(2007, 2020):
                for quarter in range(1, 5):
                    if obj.stock_code.startswith('6'):
                        rs_profit = bs.query_balance_data(code="sh.{}".format(obj.stock_code), year=year, quarter=quarter)
                    else:
                        rs_profit = bs.query_balance_data(code="sz.{}".format(obj.stock_code), year=year, quarter=quarter)
                    while (rs_profit.error_code == '0') & rs_profit.next():
                            balance_list.append(rs_profit.get_row_data())
            result_profit = pd.DataFrame(balance_list, columns=rs_profit.fields).values
            for item in result_profit:
                if any([item[3], item[4], item[5], item[6], item[7], item[8]]):
                    ag = AStocksBalance()
                    ag.stock = obj
                    ag.pub_date = item[1]
                    ag.stat_date = item[2]
                    ag.current_ratio = float(item[3]) if item[3] else 0.0
                    ag.quick_ratio = float(item[4]) if item[4] else 0.0
                    ag.cash_ratio = float(item[5]) if item[5] else 0.0
                    ag.yoy_liability = float(item[6]) if item[6] else 0.0
                    ag.liability_to_asset = float(item[7]) if item[7] else 0.0
                    ag.asset_to_equity = float(item[8]) if item[8] else 0.0
                    ag.save()
        except:
            # 保存出错的股票代码
            error_code.append(obj.stock_code)
            continue

    print('import finish, need time: ', time()-start)
    print('Error code: ', error_code)
    bs.logout()


if __name__ == '__main__':
    query_balance()