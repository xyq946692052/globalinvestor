import json
from django.shortcuts import render

from cn_a_stocks.models import AStocksEarnRate

def home(request):
    context = dict()

    ae = AStocksEarnRate.objects.first()
    context['one_month'] = json.loads(ae.one_month)
    context['three_month'] = json.loads(ae.three_month)
    context['half_year'] = json.loads(ae.half_year)
    context['one_year'] = json.loads(ae.one_year)
    context['three_year'] = json.loads(ae.three_year)
    context['five_year'] = json.loads(ae.five_year)
    context['ten_year'] = json.loads(ae.ten_year)

    return render(request, 'home.html', context)


