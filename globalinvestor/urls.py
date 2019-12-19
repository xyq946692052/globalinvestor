"""globalinvestor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.urls import path, include

from globalinvestor import views

urlpatterns = [
    path(r'xadmin/', xadmin.site.urls, name='xadmin'),
    path('', views.home, name='home'),
    path('cn_a_stocks/', include('cn_a_stocks.urls')),
    path('cn_hk_stocks/', include('cn_hk_stocks.urls')),
    path('us_stocks/', include('us_stocks.urls')),
    path('cryptocurrency/', include('cryptocurrency.urls')),
]

# 处理404，500错误， 需要在配置文件中设置DEBUG=False才能生效
handler404 = views.page_not_found
handler500 = views.page_error
