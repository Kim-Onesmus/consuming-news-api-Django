from django.shortcuts import render
import requests

# Create your views here.
API_KEY = 'aeeace275047440788ac8885dd143e23'

def Home(request):
    url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-03-07&sortBy=publishedAt&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    print(data)

    context = {
        'data':data
    }
    return render(request, 'app/home.html', context)