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



def update_category_with_csvfile(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        res = csv.reader(f)
        for k in res:
            sc = AStocksCategory()
            sc.id = k[0]
            sc.category_name = k[1]
            sc.save()
    print('inport finished...')


def import_category_with_api():
    import tushare as ts
    pro = ts.pro_api('15ff201419345eabb82bb14409b7b0cb8f9eee89744fabd37119d015')
    datas = pro.query('stock_basic', exchange='', list_status='L',
                      fields='ts_code,symbol,name,area,industry,list_date').values
    categorys = list(set(item[4] for item in datas if item[4] != None))

    for item in categorys:
        cv = AStocksCategory()
        cv.category_name = item
        cv.save()
    print('finished...')


def import_stocks_code_name_area_with_api():
    import tushare as ts
    pro = ts.pro_api('15ff201419345eabb82bb14409b7b0cb8f9eee89744fabd37119d015')
    datas = pro.query('stock_basic', exchange='', list_status='L',
                      fields='ts_code,symbol,name,area,industry,list_date').values
    for index, item in enumerate(datas):
        print(index)
        ac = AStocksCategory.objects.filter(category_name=item[4]).first()
        ah = AStocksHeader()
        ah.stock_code = item[1]
        ah.stock_name = item[2]
        ah.area = item[3]
        ah.category = ac
        ah.save()

    print('import finish...')

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


def update_header_with_csvfile(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        res = csv.reader(f)
        for k in res:
            ct = AStocksCategory.objects.get(pk=k[3])
            sh = AStocksHeader()
            ipodate = "-".join([k[5].split('/')[2],k[5].split('/')[1],k[5].split('/')[0]])
            outdate = "-".join([k[6].split('/')[2],k[6].split('/')[1],k[5].split('/')[0]])
            sh.id = k[0]
            sh.stock_name = k[1]
            sh.stock_code=k[2]
            sh.category = ct
            sh.area = k[4]
            sh.ipodate=ipodate
            sh.outdate=outdate
            sh.isdelisted=k[7]
            sh.save()

    print('inport finished...')


def getStockBaseInfo():
    pro = ts.pro_api('15ff201419345eabb82bb14409b7b0cb8f9eee89744fabd37119d015')
    # 交易所代码 ，SSE上交所 SZSE深交所 ，默认SSE
    df = pro.stock_company(exchange='SZSE', fields='ts_code,reg_capital,website,business_scope,main_business,introduction').values
    res = []
    count = 0
    for code, reg_capital,introduction,website,business_scope,main_business in df:
        print(count)
        ah = AStocksHeader.objects.filter(stock_code=code.split('.')[0]).first()
        if ah:
            ah.reg_capital = reg_capital
            ah.website = website
            ah.main_business = main_business
            ah.business_scope = business_scope
            ah.introduction = introduction
            ah.save()
        else:
            res.append(code.split('.')[0])
        count += 1
    print('==========finished!')




if __name__ == '__main__':
    #import_category_with_api()
    #import_stocks_code_name_area_with_api()
    getStockBaseInfo()
    #update_ipodate()
    #update_category_with_csvfile('stocks_a_category.csv')
    #getStockBaseInfo()
    #update_header_with_csvfile('stocks_a_header.csv')
    #get_all_stocks()
    #import_category_with_api()
