from django.urls import path

from . import api_endpoints as views

app_name = 'news'

urlpatterns = [
    path('list/', views.NewsListAPIView.as_view(), name='news_list'),
    path('retrieve/<int:pk>/', views.NewsRetrieveAPIView.as_view(), name='news_retrieve'),
]
