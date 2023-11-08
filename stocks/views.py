from django.shortcuts import render
# from django.http import HttpResponse
import requests
import json
from .api_key import key

def home(request):
    try:
        ticker = request.GET['ticker']
        # stock_api = requests.get(f"https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token={key}")
        stock_api = requests.get(f"https://cloud.iexapis.com/stable/stock/{ticker}/quote?token={key}")
        stock = json.loads(stock_api.content)
    except Exception as e:
        stock = ""


    content = {'stock' : stock}

    return render(request, 'stocks/home.html', content) # 이제 home.html 에서 content의 내용을 쓸 수 있다.
