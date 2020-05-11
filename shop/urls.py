from django.urls import path
from . import views

# http://localhost:8000
# http://localhost:8000/type/1
# http://localhost:8000/type/shop/1
# http://localhost:8000/1/1
# 

# start with shop
urlpatterns = [
    # http://localhost:8000/shop/1
    path('', views.shop_list, name='shop_list'),
    path('<int:shop_pk>', views.shop_detail, name='shop_detail'),
    path('type/<int:shop_type_pk>', views.shop_with_type, name='shop_with_type'),
]