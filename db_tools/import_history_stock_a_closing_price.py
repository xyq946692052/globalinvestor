# @File  : $import_stock_a_closing_price.py
# @Author: kevin.xie
# @Date  : 2020/03/11
# @Desc  : 运行此文件即可通过查询接口导入股票至今的收盘价

import os
import sys
import baostock as bs
from time import time
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "globalinvestor.conf.test")
import django
django.setup()

from cn_a_stocks.models import AStocksHeader, AStocksCategory,AStocksClsePrice



def import_closing_price():
    lg = bs.login()
    shobjs = AStocksHeader.objects.all()
    count = 0
    start = time()
    current_date = datetime.now().strftime('%Y-%m-%d')
    print('start import...')
    for obj in shobjs:
        acp = AStocksClsePrice.objects.filter(stock=obj).last()
        start_date = acp.exchange_date.strftime('%Y-%m-%d')  # 获取该股票最后的导入时间，作为新的开始导入时间

        if current_date != start_date:
            if obj.stock_code.startswith("6"):
                rs = bs.query_history_k_data_plus("sh.{}".format(obj.stock_code),
                    "date, code, close, peTTM, pbMRQ, psTTM, pcfNcfTTM",
                    start_date=start_date, end_date=current_date,
                    frequency="d", adjustflag="3")
            else:
                rs = bs.query_history_k_data_plus("sz.{}".format(obj.stock_code),
                   "date, code, close, peTTM, pbMRQ, psTTM, pcfNcfTTM",
                   start_date=start_date, end_date=current_date,
                   frequency="d", adjustflag="3")

            result_list = []
            while (rs.error_code == '0') & rs.next():
                result_list.append(rs.get_row_data())

            sh_lst = AStocksHeader.objects.all()
            sh_dic, data = {}, {}
            for sh in sh_lst:
                sh_dic[sh.stock_code] = sh.id

            for changedate, code, closeprice, _, _, _, _ in result_list:
                stock_code = code.split(".")[1]
                data['stock_id'] = sh_dic.get(stock_code)
                data['exchange_date'] = changedate
                data['closing_price'] = closeprice
                AStocksClsePrice.objects.create(**data)
            count += 1
            print(f'----------{count}  {acp}, -最新收盘价导入完成')
    print("need time: ", time()-start)
    bs.logout()


if __name__ == '__main__':
    import_closing_price()