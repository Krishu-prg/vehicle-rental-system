from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Vehicle, Customer, Rental
from .forms import VehicleForm, CustomerForm, RentalForm

def dashboard(request):
    vehicles_count = Vehicle.objects.count()
    available_count = Vehicle.objects.filter(status='available').count()
    rented_count = Vehicle.objects.filter(status='rented').count()
    customers_count = Customer.objects.count()
    recent_rentals = Rental.objects.order_by('-rent_date')[:5]
    
    context = {
        'vehicles_count': vehicles_count,
        'available_count': available_count,
        'rented_count': rented_count,
        'customers_count': customers_count,
        'recent_rentals': recent_rentals,
    }
    return render(request, 'rental_app/dashboard.html', context)

# Vehicle Views
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'rental_app/vehicle_list.html', {'vehicles': vehicles})

def vehicle_add(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehicle added successfully!')
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'rental_app/vehicle_form.html', {'form': form, 'title': 'Add Vehicle'})

def vehicle_edit(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehicle updated successfully!')
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'rental_app/vehicle_form.html', {'form': form, 'title': 'Edit Vehicle'})

def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    vehicle.delete()
    messages.success(request, 'Vehicle deleted successfully!')
    return redirect('vehicle_list')

# Customer Views
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'rental_app/customer_list.html', {'customers': customers})

def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer added successfully!')
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'rental_app/customer_form.html', {'form': form})

# Rental Views
def rental_list(request):
    rentals = Rental.objects.all().order_by('-rent_date')
    return render(request, 'rental_app/rental_list.html', {'rentals': rentals})

def rental_add(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rental record created successfully!')
            return redirect('vehicle_list')
    else:
        form = RentalForm()
    return render(request, 'rental_app/rental_form.html', {'form': form})

def rental_return(request, pk):
    rental = get_object_or_404(Rental, pk=pk)
    if rental.return_date:
        messages.warning(request, 'This vehicle has already been returned.')
    else:
        rental.return_date = timezone.now().date()
        rental.vehicle.status = 'available'
        rental.vehicle.save()
        
        # Calculate total cost (simple: days * price_per_day)
        delta = rental.return_date - rental.rent_date
        days = max(delta.days, 1) # Minimum 1 day cost
        rental.total_cost = days * rental.vehicle.price_per_day
        rental.save()
        
        messages.success(request, f'Vehicle returned! Total cost: {rental.total_cost}')
    return redirect('rental_list')
