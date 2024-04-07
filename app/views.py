from django.shortcuts import render
import requests

# Create your views here.
API_KEY = ''

def Home(request):
    country = request.GET.get('country')

    category = request.GET.get('category')
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context = {
        'data':data,
        'articles':articles
    }
    return render(request, 'app/home.html', context)