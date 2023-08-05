from django.urls import path

from . import api_endpoints as views

app_name = 'cart'

urlpatterns = [
    path('cart_items/list/', views.CartItemListAPIView.as_view(), name='cart_item_list'),
    path('cart_items/create_update/', views.CartItemNoAuthCreateUpdateAPIView.as_view(), name='cart_item_create'),
    path('cart_items/delete/all/', views.CartItemDeleteAllAPIView.as_view(), name='cart_item_delete_all'),
    path('cart_items/delete/<int:pk>/', views.CartItemDeleteAPIView.as_view(), name='cart_item_delete')
]
