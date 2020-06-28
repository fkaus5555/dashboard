
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","websaver.settings")
import django
django.setup()

def info__():
    url = "https://finance.naver.com/item/main.nhn?code=036570"
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    table = bs_obj.find("table", {"class": "tb_type1 tb_num tb_type1_ifrs"}) # 태그 p, 속성값 no_today 찾기
    return table


 

