from django.urls import path

from . import api_endpoints as views

app_name = 'cart'

urlpatterns = [
    path('cart_items/list/', views.CartItemNoAuthListAPIView.as_view(), name='cart_item_no_auth_list'),
    path('cart_items/create_update/', views.CartItemNoAuthCreateUpdateAPIView.as_view(), name='cart_item_no_auth_create'),
    path('cart_items/delete/<int:pk>/', views.CartItemNoAuthDeleteAPIView.as_view(), name='cart_item_no_auth_delete')
]
