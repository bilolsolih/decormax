from django.urls import path

from . import api_endpoints as views

app_name = 'store'

urlpatterns = [
    path('colors/list/', views.ColorListAPIView.as_view(), name='color_list'),
    path('picture_types/list/', views.PictureTypeListAPIView.as_view(), name='picture_type_list'),
    path('sizes/list/', views.SizeListAPIView.as_view(), name='size_list'),
    path('stores/list/', views.SizeListAPIView.as_view(), name='size_list'),
    path('styles/list/', views.StyleListAPIView.as_view(), name='style_list'),
    path('target_rooms/list/', views.TargetRoomListAPIView.as_view(), name='target_room_list'),
    path('products/list/', views.ProductListAPIView.as_view(), name='product_list'),
    path('products/retrieve/<int:pk>/', views.ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    # path('manufacturing_methods/list', views.ManufacturingMethodListAPIView.as_view(), name='manufacturing_methods_list'),
    path('collections/list/', views.CollectionListAPIView.as_view(), name='collection_list'),
    path('building_materials/list/', views.BuildingMaterialListAPIView.as_view(), name='building_material_list'),
    # path('brands/list/', views.BrandListAPIView.as_view(), name='brand_list'),
]
