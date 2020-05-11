import datetime
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from read_statistics.utils import get_seven_days_read_data, get_today_hot_data, get_yesterday_hot_data
from shop.models import Shop

def get_seven_days_hot_shops():  #最近七天最热店铺
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    shops = Shop.objects.filter(read_details__date__lt=today, read_details__date__gte=date).values('id', 'name').annotate(read_num_sum=Sum('read_details__read_num')).order_by('-read_num_sum')
    return shops[:7]

def home(request):
    shop_content_type = ContentType.objects.get_for_model(Shop)
    dates, read_nums = get_seven_days_read_data(shop_content_type)

    context = {}
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['today_hot_data'] = get_today_hot_data(shop_content_type)
    context['yesterday_hot_data'] = get_yesterday_hot_data(shop_content_type)
    context['seven_days_hot_shops'] = get_seven_days_hot_shops()
    return render(request, 'home.html', context)
