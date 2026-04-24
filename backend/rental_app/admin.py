from django.contrib import admin
from .models import Vehicle, Customer, Rental

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'vehicle_type', 'price_per_day', 'status')
    list_filter = ('vehicle_type', 'status')
    search_fields = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'customer', 'rent_date', 'return_date', 'total_cost')
    list_filter = ('rent_date', 'return_date')
    search_fields = ('vehicle__name', 'customer__name')
