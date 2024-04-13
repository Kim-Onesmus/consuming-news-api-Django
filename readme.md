<h1>Consuming News API in django</h1>
<p>This project guide explains how to consume a News API in a Django project. By integrating a News API into your Django application, you can fetch and display news articles from various sources, categories, and topics.</p>


<h3>To install</h3>
-Clone the project to your machine <br>
```git clone https://github.com/Kim-Onesmus/consuming-news-api-Django.git```


-Go to <a href="https://newsapi.org/">https://newsapi.org/</a> create an account and click get API Key
-Copy api key and paste it in the views.py

-Create a virtual environment<br>
```python -m venv .venv```


-Activate virtual environment<br>
```.\.venv\Scripts\activate```


-Install requirements<br>
```pip install -r requirements.txt```


-Run your code<br>
```python manage.py runserver```



-Open your browser and type<br>
```http://127.0.0.1:8000/```

You can filter the news by: <br>
    1. Country <br>
    ```http://127.0.0.1:8000/?country=us``` <br>
    2. Category <br>
    ```http://127.0.0.1:8000/?category=Business```<br>
    

😎Happy coding😎
