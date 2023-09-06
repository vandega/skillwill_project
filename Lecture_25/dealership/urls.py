from django.urls import path
from . import views

urlpatterns = [
    # car urls
    path('car/', views.car_list, name='car_list'),
    path('car/new/', views.create_car, name='create_car'),
    path('car/<int:pk>', views.car_details, name='car_details'),


    # model urls
    path('brand/', views.brand_list, name='brand_list'),
    path('brand/new/', views.create_brand, name='create_brand'),

    # dealer urls
    path('dealer/', views.dealer_list, name='dealers_list'),
    path('dealer/new/', views.create_dealer, name='create_dealer'),
    path('dealer/<int:pk>/', views.dealer_details, name='dealer_details')
]