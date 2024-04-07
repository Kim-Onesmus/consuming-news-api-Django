from django.shortcuts import render
from django.conf import settings
import requests
# Create your views here.

news_url = settings.URL

def Home(request):
    country = request.GET.get('country')

    category = request.GET.get('category')
    if country:
        url = news_url
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif category:
        url = news_url
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