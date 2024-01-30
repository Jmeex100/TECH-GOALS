from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import datetime

# Create your views here.

def index(request):
    today = datetime.today().strftime('%y-%m-%d')
    
    url = f'https://apiv3.apifootball.com/?action=get_events&league_id=149&from={today}&to={today}&APIkey=8556a506a91c36c8d01cb75da97f1eb4c5ffaa899c31d39d4a5c2a2e13800faf'
    response = requests.get(url)
    
    jsonResponce = response.json()
    
    
    return render(request,'website/index.html',{'jsonResponce':jsonResponce})
  

def new(request):
    
    
    
    return HttpResponse(' new views')



def article(request,article_id):
      return render(request,'website/index.html',{'article_id':article_id})