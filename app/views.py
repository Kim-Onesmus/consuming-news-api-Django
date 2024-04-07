from django.shortcuts import render
import requests
from . import env
# Create your views here.


def Home(request):
    country = request.GET.get('country')

    category = request.GET.get('category')
    if country:
        url = env.url
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif category:
        url = env.url
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = env.url
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context = {
        'data':data,
        'articles':articles
    }
    return render(request, 'app/home.html', context)