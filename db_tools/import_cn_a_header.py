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

from cn_a_stocks.models import AStocksHeader, AStocksCategory


#更新地区数据
def update_area():
    datas = ts.get_stock_basics().values
    for index, item in enumerate(datas):
        print(index, item[0])
        shobj = AStocksHeader.objects.filter(stock_name=item[0]).first()
        if shobj:
            shobj.area = item[2]
            shobj.save()
    print('finish updated...')



#更新上市时间,退市时间，以及是否是退市股
def update_ipodate():
    data_list = []
    lg = bs.login()
    shobj = AStocksHeader.objects.all()
    for obj in shobj:
        rs = bs.query_stock_basic(code_name=obj.stock_name)
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
    for index, item in enumerate(data_list):
        sb = AStocksHeader.objects.filter(stock_name=item[1]).first()
        if sb:
            print(index, item[1])
            sb.ipodate = item[2]
            if item[3] != '':
                sb.outdate = item[3]
                sb.isdelisted = True
            sb.save()
    print('update finished...')
    bs.logout()


def update_category_with_csvfile(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        res = csv.reader(f)
        for k in res:
            sc = AStocksCategory()
            sc.id = k[0]
            sc.category_name = k[1]
    print('inport finished...')


def update_header_with_csvfile(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        res = csv.reader(f)
        for k in res:
            sh = AStocksHeader()
            sh.id = k[0]
            sh.stock_name = k[1]
            sh.stock_code=k[2]
            sh.category = k[3]
            sh.area = k[4]
            sh.ipodate=k[5]
            sh.outdate=k[6]
            sh.isdelisted=k[7]
    print('inport finished...')


def getStockBaseInfo():
    pro = ts.pro_api('15ff201419345eabb82bb14409b7b0cb8f9eee89744fabd37119d015')
    df = pro.stock_company(exchange='SZSE', fields='ts_code,reg_capital,website,business_scope,main_business,introduction').values
    res = []
    count = 0
    for code, reg_capital,introduction,website,business_scope,main_business in df:
        #print('------', code,'===', reg_capital,'===', introduction,'===',website,'===',business_scope, '===',main_business)
        print(count)
        ah = AStocksHeader.objects.filter(stock_code=code.split('.')[0]).first()
        if ah:
            ah.reg_capital = reg_capital
            ah.website = website
            ah.main_business = main_business
            ah.business_scope = business_scope
            ah.introduction = introduction
            #ah.save()
        else:
            res.append(code.split('.')[0])
        count += 1
    with open('res.txt', 'w') as f:
        res = ','.join(res)
        f.writelines(res)
    print('==========finished!')



if __name__ == '__main__':
    #update_ipodate()
    #update_category_with_csvfile('stocks_a_category.csv')
    getStockBaseInfo()