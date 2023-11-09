from django.urls import path,include
from Crypto import views

app_name = 'Crypto'
urlpatterns = [
    path('',views.index,name='index'),
]


