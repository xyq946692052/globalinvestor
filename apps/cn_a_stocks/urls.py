from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail', views.detail, name='detail'),
    path('ajax_getstocks_by_category', views.ajax_getstocks_by_category),
]
