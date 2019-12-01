from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'cn_hk_stocks/index.html', context)