# views = 만들어진 기능을 받아와서 템플릿에 전달
from django.http import HttpResponse
from django.shortcuts import render

import requests
import json#정보 처리
from bs4 import BeautifulSoup
from stock.models import stockData_sam, stockData_lg, stockData_naver, stockData_kakao, stockData_nc, user_post
from .forms import form_form


def stock(request):
	api_requests1 = requests.get('https://cloud.iexapis.com/stable/stock/ssnlf/book?token=pk_725a140958924080af2a48b9efd852fa')
	api_requests2 = requests.get('https://cloud.iexapis.com/stable/stock/msft/book?token=pk_725a140958924080af2a48b9efd852fa')
	api_requests3 = requests.get('https://cloud.iexapis.com/stable/stock/googl/book?token=pk_725a140958924080af2a48b9efd852fa')
	api_requests4 = requests.get('https://cloud.iexapis.com/stable/stock/nflx/book?token=pk_725a140958924080af2a48b9efd852fa')
	api_requests5 = requests.get('https://cloud.iexapis.com/stable/stock/fb/book?token=pk_725a140958924080af2a48b9efd852fa')



	try :
		api1 = json.loads(api_requests1.content)
		api2 = json.loads(api_requests2.content)
		api3 = json.loads(api_requests3.content)
		api4 = json.loads(api_requests4.content)
		api5 = json.loads(api_requests5.content)


	except Exception as e:
		api1 = e

	return render(request,'stock.html', {'stock_info1' : api1, 'stock_info2' : api2,'stock_info3' : api3,'stock_info4' : api4,'stock_info5' : api5})


def home(request):
	return render(request, 'home.html', {})

def stock_croll(stock_num):
	url = "https://finance.naver.com/item/main.nhn?code="+stock_num
	result = requests.get(url)
	bs_obj = BeautifulSoup(result.content, "html.parser")

	blind = bs_obj.find("dl", {"class": "blind"})  # 태그 dl, 속성값 blind 찾기
	#현재가
	no_today = bs_obj.find("p", {"class": "no_today"})  # 태그 p, 속성값 no_today 찾기
	blindd = no_today.find("span", {"class": "blind"})  # 태그 span, 속성값 blind 찾기
	now_price = blindd.text
	# 52주 최고최저부터 추출
	week52 = bs_obj.find("table", {"class": "rwidth"})
	week5252 = week52.find_all("em")
	high52 = week5252[2]
	low52 = week5252[3]
	high52 = high52.text
	low52 = low52.text

	# 리스트로 나눠
	r_blind = blind.text
	r_blind = r_blind.replace('\n', ' ')
	r_blind = r_blind.split(" ")

	# 리스트 인덱스 가져오고
	name1_num = r_blind.index("종목명")
	name2_num = name1_num + 1
	last1_num = r_blind.index("전일가")
	last2_num = last1_num + 1
	start1_num = r_blind.index("시가")
	start2_num = start1_num + 1
	high1_num = r_blind.index("고가")
	high2_num = high1_num + 1
	low1_num = r_blind.index("저가")
	low2_num = low1_num + 1
	vol1_num = r_blind.index("거래량")
	vol2_num = vol1_num + 1

	# 딕셔너리로 만들
	stock = {r_blind[name1_num]: r_blind[name2_num],
			 r_blind[last1_num]: r_blind[last2_num],
			 r_blind[start1_num]: r_blind[start2_num],
			 "종가": now_price,
			 r_blind[high1_num]: r_blind[high2_num],
			 r_blind[low1_num]: r_blind[low2_num],
			 r_blind[vol1_num]: r_blind[vol2_num],
			 "52주최고": high52, "52주최저": low52}
	return stock


# 종목명 전일가 시작가격 종료가격 최고 최저 거래량 52주고 52주저

# 종목명, 전일가, 시가, 전일가(실제는 종가), 고가, 저가, 거래량, 52주 최고, 52주 최저


def kor_stock(request):
	#삼성전자 : 005930
	#lg전자 : 066570
	#네이버 : 035420
	#카카오 : 035720
	#엔씨소프트 : 036570
	stock1 = stock_croll("005930")
	stock2 = stock_croll("066570")
	stock3 = stock_croll("035420")
	stock4 = stock_croll("035720")
	stock5 = stock_croll("036570")


	stock={"1":stock1,"2":stock2, "3": stock3,
		   "4":stock4,"5":stock5}


	return render(request, 'kor_stock.html', stock)
def info_1(num):
	url = "https://finance.naver.com/item/main.nhn?code="
	url=url+num
	result = requests.get(url)
	bs_obj = BeautifulSoup(result.content, "html.parser")
	table = bs_obj.find("table", {"class": "tb_type1 tb_num tb_type1_ifrs"})  # 태그 p, 속성값 no_today 찾기

	table = str(table)
	table = table.replace("기업실적분석", num+" 기업실적분석")
	table=table.replace("class=", "border = 1 ")
	return(table)


def info_stock1(request):
	stockData_sam.objects.all().delete()
	inf = stockData_sam(title=info_1("005930"))
	inf.save()
	aa=stockData_sam.objects.all()
	return HttpResponse(aa)
def info_stock2(request):
	stockData_lg.objects.all().delete()
	inf = stockData_lg(title=info_1("066570"))
	inf.save()
	aa=stockData_lg.objects.all()
	return HttpResponse(aa)
def info_stock3(request):
	stockData_naver.objects.all().delete()
	inf = stockData_naver(title=info_1("035420"))
	inf.save()
	aa=stockData_naver.objects.all()
	return HttpResponse(aa)
def info_stock4(request):
	stockData_kakao.objects.all().delete()
	inf = stockData_kakao(title=info_1("035720"))
	inf.save()
	aa=stockData_kakao.objects.all()
	return HttpResponse(aa)
def info_stock5(request):
	stockData_nc.objects.all().delete()
	inf = stockData_nc(title=info_1("036570"))
	inf.save()
	aa=stockData_nc.objects.all()
	return HttpResponse(aa)



def form_test(request):
	forms = request.POST.get('Search')
	croll=stock_croll(forms)

	user_post.objects.all().delete()
	post = user_post(title=info_1(forms))
	post.save()

	return render(request, 'user.html', croll)

def info_stock0(request):
	aa=user_post.objects.all()
	return HttpResponse(aa)
