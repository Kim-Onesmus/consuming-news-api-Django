from django.shortcuts import render
import requests

# Create your views here.
API_KEY = 'aeeace275047440788ac8885dd143e23'

def Home(request):
    url = f'https://newsapi.org/v2/everything?q=tesla&from=2024-03-07&sortBy=publishedAt&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
        'data':data,
        'articles':articles
    }
    return render(request, 'app/home.html', context)