from django.urls import path
from .views import send_data

app_name = 'scrapper_app'
urlpatterns = [
    path('index/',send_data, name='index'),
]
