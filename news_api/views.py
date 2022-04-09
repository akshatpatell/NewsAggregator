from dataclasses import field, fields
from linecache import lazycache
from multiprocessing.spawn import import_main_path
from nturl2path import url2pathname
from re import template
from django.shortcuts import redirect, render
import requests
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
API_KEY = 'd0b69496c18e463f888a273cb521ea9f'
import news_api


# Create your views here.


    

def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    
    
    
    
    if country == "usa":
        country =  'us'
    elif country == "india":
        country = 'in'
    elif country == "china":
        country = 'cn'
    elif country == 'united kingdom':
        country = 'gb'
    elif country == 'italy':
        country = 'it'
    elif country == 'russia':
        country = 'ru'
    elif country == 'ukraine':
        country = 'ua'
    elif country == 'new zealand':
        country = 'nl'
    elif country == 'South africa':
        country = 'za'
    elif country == 'austria':
        country = 'at'
    elif country == 'canada':
        country = 'ca'
        
    
    
    

    
    
    if country:
        
        
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?q={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    


    
    context = {
        'articles' : articles
        
        
    }

    return render(request, 'news_api/home.html', context)


