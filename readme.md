<h1>Consuming News API in django</h1>
<p>This project guide explains how to consume a News API in a Django project. By integrating a News API into your Django application, you can fetch and display news articles from various sources, categories, and topics.</p>

*To install*
-Clone the project to your machine
```git clone https://github.com/Kim-Onesmus/consuming-news-api-Django.git```

-Go to <a href="https://newsapi.org/">https://newsapi.org/</a> create an account and click get API Key
-Copy api key and paste it in the views.py

-Create a virtual environment
```python -m venv .venv```

-Activate virtual environment
```.\.venv\Scripts\activate```

-Install requirements
```pip install -r requirements.txt```

-Run your code
```python manage.py runserver```

-Open your browser and type
```http://127.0.0.1:8000/```

You can filter the news by:
    1. Country
    ```http://127.0.0.1:8000/?country=us```
    2. Category
    ```http://127.0.0.1:8000/?category=Business```

😎Happy coding😎
