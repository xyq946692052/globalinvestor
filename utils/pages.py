from django.core.paginator import Paginator
from django.conf import settings


def get_page_range(request, objs):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(objs, settings.PAGINATOR_NUM)

    page_of_obj = paginator.get_page(page_num)
    obj_list = page_of_obj.object_list
   
    current_page_num = page_of_obj.number
    range_page = list(range(max(current_page_num-2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num+2, paginator.num_pages)+1))

    # 添加省略号
    if range_page[0]-1 > 2:
        range_page.insert(0, '...')
    if paginator.num_pages-range_page[-1] >= 2:
        range_page.append('...')

    # 添加首页和尾页
    if range_page[0] !=1:
        range_page.insert(0, 1)
    if range_page[-1] != paginator.num_pages:
        range_page.append(paginator.num_pages)

    return obj_list, page_of_obj, range_page

