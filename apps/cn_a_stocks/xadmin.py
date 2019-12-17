import xadmin
from xadmin import views

from .models import AStocksCategory


class BaseSetting:
    enable_themes = True  #开启主题功能
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)

@xadmin.sites
class GlobalSettings:
    site_title = 'Global Investor'
    site_footer = 'Global Investor'
    menu_style = 'STocks_a_cn'


xadmin.site.register(views.CommAdminView, GlobalSettings)


@xadmin.site.register(AStocksCategory)
class AStocksCategoryAdmin(object):
    list_display = ['id', 'category_name']
    list_filter = ['category_name']
