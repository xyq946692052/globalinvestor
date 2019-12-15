
from datetime import datetime
from time import time
from itertools import chain
from operator import itemgetter
import traceback

from django.shortcuts import render
from django.db.models import Q

from cn_a_stocks.models import AStocksClsePrice, AStocksHeader
from utils.get_yield_rate import get_nearmonth_rate
from utils.matplot_pic import draw_graph

def home(request):
    context = {}
    current_year = datetime.now().year


    ah_ids = chain(*(AStocksHeader.objects.only('id').values_list('id').all()))
    datas = []
    errlst = []
    s1 = time()
    for sid in ah_ids:
        datas.append(get_nearmonth_rate(sid))
    sorted(datas, key=itemgetter('earn_rate'))
    print(len(datas))
    for k in datas[:20]:
        print(k)
    print(time()-s1)



    return render(request, 'home.html', context)


