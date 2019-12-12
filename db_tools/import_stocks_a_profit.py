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

from cn_a_stocks.models import AStocksHeader, AStocksProfit


def query_profit():
    # 接口提供的数据最早从2007年开始
    lg = bs.login()
    shobjs = AStocksHeader.objects.all()
    count = 0
    start = time()
    for obj in shobjs:
        profit_list = []
        count += 1
        print(count)
        for year in range(2007, 2020):
            for quarter in range(1,5):
                if obj.stock_code.startswith('6'):
                    rs_profit = bs.query_profit_data(code="sh.{}".format(obj.stock_code), year=year, quarter=quarter)
                else:
                    rs_profit = bs.query_profit_data(code="sz.{}".format(obj.stock_code), year=year, quarter=quarter)
                while (rs_profit.error_code == '0') & rs_profit.next():
                        profit_list.append(rs_profit.get_row_data())
        result_profit = pd.DataFrame(profit_list, columns=rs_profit.fields).values
        for item in result_profit:
            ap = AStocksProfit()
            ap.stock = obj
            ap.pub_date = item[1]
            ap.stat_date = item[2]
            ap.roe_avg = float(item[3]) if item[3] else 0.0
            ap.np_margin = float(item[4]) if item[4] else 0.0
            ap.gp_margin = float(item[5]) if item[5] else 0.0
            ap.net_profit = float(item[6]) if item[6] else 0.0
            ap.epsttm = float(item[7]) if item[7] else 0.0
            ap.mb_revenue = float(item[8]) if item[8] else 0.0
            ap.total_share = float(item[9]) if item[9] else 0.0
            ap.liqa_share = float(item[10]) if item[10] else 0.0
            ap.save()
    print('import finish, need time: ', time()-start)
    bs.logout()


if __name__ == '__main__':
    query_profit()