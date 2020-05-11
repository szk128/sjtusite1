from django.shortcuts import render, get_object_or_404
from .models import Shop, ShopType
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from read_statistics.utils import read_statistics_once_read
# Create your views here.


def shop_list(request):
    shops_all_list = Shop.objects.all()
    paginator = Paginator(shops_all_list,6)
    page_num = request.GET.get('page',1)
    page_of_shops = paginator.get_page(page_num)
    current_page_num = page_of_shops.number
    page_range = list(range(max(current_page_num - 2, 1), min(paginator.num_pages + 1, current_page_num + 3)))

    if page_range[0]-1>=2:
        page_range.insert(0,'...')
    if paginator.num_pages-page_range[-1]>=2:
        page_range.append('...')

    if page_range[0] != 1:
        page_range.insert(0,1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)


    context = {}
    context['shops'] = page_of_shops.object_list
    context['page_of_shops'] = page_of_shops
    context['page_range'] = page_range
    context['shop_types'] =  ShopType.objects.all()
    return render(request, 'shop/shop_list.html',context)

def shop_detail(request, shop_pk):
    shop = get_object_or_404(Shop, pk=shop_pk)
    read_cookie_key = read_statistics_once_read(request, shop)
    context = {}
    context['shop'] = shop
    response = render(request, 'shop/shop_detail.html',context) #响应
    response.set_cookie(read_cookie_key, 'true')

    return response

def shop_with_type(request,shop_type_pk):

    context = {}
    shop_type = get_object_or_404(ShopType, pk=shop_type_pk)

    shops_all_list = Shop.objects.filter(shop_type=shop_type)
    paginator = Paginator(shops_all_list,6)
    page_num = request.GET.get('page',1)
    page_of_shops = paginator.get_page(page_num)
    current_page_num = page_of_shops.number
    page_range = list(range(max(current_page_num - 2, 1), min(paginator.num_pages + 1, current_page_num + 3)))

    if page_range[0]-1>=2:
        page_range.insert(0,'...')
    if paginator.num_pages-page_range[-1]>=2:
        page_range.append('...')

    if page_range[0] != 1:
        page_range.insert(0,1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)


    context = {}
    context['shop_type'] = shop_type
    context['shops'] = page_of_shops.object_list
    context['page_of_shops'] = page_of_shops
    context['page_range'] = page_range
    context['shop_types'] =  ShopType.objects.all()
    return render(request, 'shop/shops_with_type.html', context)