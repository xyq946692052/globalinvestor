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

from cn_a_stocks.models import AStocksHeader, AStocksOperation


def import_data():
    # 接口提供的数据最早从2007年开始
    lg = bs.login()


    shobjs = AStocksHeader.objects.all()
    count = 0
    start = time()
    for obj in shobjs:
        operation_list = []
        count += 1
        print(count)
        for year in range(2007, 2020):
            for quarter in range(1,5):
                if obj.stock_code.startswith('6'):
                    rs_operation = bs.query_operation_data(code="sh.{}".format(obj.stock_code), year=year, quarter=quarter)
                else:
                    rs_operation = bs.query_operation_data(code="sz.{}".format(obj.stock_code), year=year, quarter=quarter)
                while (rs_operation.error_code == '0') & rs_operation.next():
                    operation_list.append(rs_operation.get_row_data())
        result_operation = pd.DataFrame(operation_list, columns=rs_operation.fields).values
        for item in result_operation:
            if any([item[3],item[4],item[5],item[6], item[7], item[8]]):
                ao = AStocksOperation()
                ao.stock = obj
                ao.pub_date = item[1]
                ao.stat_date = item[2]
                ao.nr_turn_ratio = float(item[3]) if item[3] else 0.0
                ao.nr_turn_days = float(item[4]) if item[4] else 0.0
                ao.inv_turn_ratio = float(item[5]) if item[5] else 0.0
                ao.inv_turn_days = float(item[6]) if item[6] else 0.0
                ao.ca_turn_ratio = float(item[7]) if item[7] else 0.0
                ao.asset_turn_ratio = float(item[8]) if item[8] else 0.0
                if item[1].split("-")[0] == item[2].split("-")[0]:
                    ao.is_year_report = False
                else:
                    ao.is_year_report = True
                ao.save()
    print('import finish, need_time: ', time()-start)
    bs.logout()


if __name__ == '__main__':
    import_data()