import json
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt

from cn_a_stocks.models import AStocksEarnRate

@csrf_exempt
def page_not_found(request, exception):
    response = render_to_response('404.html')
    response.status_code = 404
    return response


@csrf_exempt
def page_error(request, exception):
    response =  render_to_response('500.html')
    response.status_code = 500
    return response


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


