from django.urls import path

from . import api_endpoints as views

app_name = 'about'

urlpatterns = [
    path('addresses/', views.AddressListAPIView.as_view(), name='address_list'),
    path('company_stats/', views.CompanyStatListAPIView.as_view(), name='company_stat'),
    path('company_histories/', views.CompanyHistoryListAPIView.as_view(), name='company_history'),
    path('emails/', views.EmailListAPIView.as_view(), name='email_list'),
    path('phone_numbers/', views.PhoneNumberListView.as_view(), name='phone_number_list'),
    path('social_medias/', views.SocialMediaListAPIView.as_view(), name='social_media_list')
]
