from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'cn_a_stocks/index.html', context)