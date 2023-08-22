from django.urls import path

from . import api_endpoints as views

app_name = 'store'

urlpatterns = [
    path('colors/list/', views.ColorListAPIView.as_view(), name='color_list'),
    path('picture_types/list/', views.PictureTypeListAPIView.as_view(), name='picture_type_list'),
    path('sizes/list/', views.SizeListAPIView.as_view(), name='size_list'),
    path('stores/list/', views.StoreListAPIView.as_view(), name='store_list'),
    path('styles/list/', views.StyleListAPIView.as_view(), name='style_list'),
    path('target_rooms/list/', views.TargetRoomListAPIView.as_view(), name='target_room_list'),
    path('collections/list/', views.CollectionListAPIView.as_view(), name='collection_list'),
    path('collections/retrieve/<int:pk>/', views.CollectionRetrieveAPIView.as_view(), name='collection_retrieve'),
    path('building_materials/list/', views.BuildingMaterialListAPIView.as_view(), name='building_material_list'),
]
