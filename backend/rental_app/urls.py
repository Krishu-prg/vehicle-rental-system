from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    # Vehicle URLs
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('vehicles/add/', views.vehicle_add, name='vehicle_add'),
    path('vehicles/edit/<int:pk>/', views.vehicle_edit, name='vehicle_edit'),
    path('vehicles/delete/<int:pk>/', views.vehicle_delete, name='vehicle_delete'),
    
    # Customer URLs
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.customer_add, name='customer_add'),
    
    # Rental URLs
    path('rentals/', views.rental_list, name='rental_list'),
    path('rentals/add/', views.rental_add, name='rental_add'),
    path('rentals/return/<int:pk>/', views.rental_return, name='rental_return'),
]
