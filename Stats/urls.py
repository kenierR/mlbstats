
from django.urls import path,include
from Stats import views
#direccion es del proyecto
urlpatterns = [
    path('index/',views.index,name='index')
]

