from django.template.defaulttags import url
from django.urls import path
from . import views

from django.urls import path
from . import views


app_name='stock'

urlpatterns = [
    path('', views.home, name="home"),
    path('stock', views.stock, name="stock"),
    path('kor_stock', views.kor_stock, name="kor_stock"),
    path('info_stock1',views.info_stock1, name="info_stock1"),
    path('info_stock2',views.info_stock2, name="info_stock2"),
    path('info_stock3',views.info_stock3, name="info_stock3"),
    path('info_stock4',views.info_stock4, name="info_stock4"),
    path('info_stock5',views.info_stock5, name="info_stock5"),
    path('ABC', views.form_test, name="from_test"),
    path('info_stock0',views.info_stock0, name="info_stock0"),
]
