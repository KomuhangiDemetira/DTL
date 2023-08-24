from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('data_collect/', views.data_collect, name='data_collect'),    
]


