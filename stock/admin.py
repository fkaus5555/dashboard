from django.contrib import admin

# Register your models here.
from django.contrib import admin
from stock.models import stockData_sam,stockData_lg, stockData_naver, stockData_kakao, stockData_nc, user_post

admin.site.register(stockData_sam)
admin.site.register(stockData_lg)
admin.site.register(stockData_naver)
admin.site.register(stockData_kakao)
admin.site.register(stockData_nc)
admin.site.register(user_post)