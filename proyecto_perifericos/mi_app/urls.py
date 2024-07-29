from django.urls import path
from mi_app import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('products/', views.product_list, name="products"),
]

formularios = [
    path('create-order/', views.create_order, name='create_order'),
    path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('query-order/', views.query_order, name='query_order'),
]

urlpatterns += formularios


