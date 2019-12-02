from django.shortcuts import render

from .models import AStocksCategory, AStocksHeader
from utils import pages


def index(request):
    context = {}
    sh_objs = AStocksHeader.objects.all()

    context['sh'], context['page_of_obj'], context['range_page'] = \
        pages.get_page_range(request, sh_objs)

    return render(request, 'cn_a_stocks/index.html', context)