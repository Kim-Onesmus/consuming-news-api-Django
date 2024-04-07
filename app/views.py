from django.shortcuts import render
from django.conf import settings
import requests
# Create your views here.

news_url = settings.API_URL
country_url = settings.COUNTRY_URL
category_url = settings.CATEGORY_URL

def Home(request):
    country = request.GET.get('country')

    category = request.GET.get('category')
    if country:
        url = country_url
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif category:
        url = category_url
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = news_url
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context = {
        'data':data,
        'articles':articles
    }
    return render(request, 'app/home.html', context)