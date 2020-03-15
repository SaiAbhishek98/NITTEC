from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'ActComLog'

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_data/', views.submit_data, name ='submit_data'),
]