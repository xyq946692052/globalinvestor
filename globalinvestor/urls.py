import xadmin
from django.urls import path, include

from globalinvestor import views

urlpatterns = [
    path(r'xadmin/', xadmin.site.urls, name='xadmin'),
    path('', views.home, name='home'),
    path('system_manager/', views.system_manager, name='system_manager'),
    path('process_schedule/', views.process_schedule, name='process_schedule'),
    path('cn_a_stocks/', include('cn_a_stocks.urls')),
    path('cn_hk_stocks/', include('cn_hk_stocks.urls')),
    path('us_stocks/', include('us_stocks.urls')),
    path('cryptocurrency/', include('cryptocurrency.urls')),
]

# 处理404，500错误， 需要在配置文件中设置DEBUG=False才能生效
handler404 = views.page_not_found
handler500 = views.page_error
