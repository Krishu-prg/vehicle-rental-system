from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Vehicle(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('rented', 'Rented'),
    ]
    
    VEHICLE_TYPES = [
        ('car', 'Car'),
        ('bike', 'Bike'),
        ('truck', 'Truck'),
        ('suv', 'SUV'),
    ]

    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    image_url = models.URLField(blank=True, null=True, help_text="Optional image URL")

    def __str__(self):
        return f"{self.name} ({self.get_vehicle_type_display()})"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class Rental(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='rentals', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='rentals', on_delete=models.CASCADE)
    rent_date = models.DateField(default=timezone.now)
    return_date = models.DateField(null=True, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.customer.name} rented {self.vehicle.name}"

    def clean(self):
        if not self.pk and self.vehicle.status == 'rented':
            raise ValidationError("This vehicle is already rented.")
        if self.return_date and self.return_date < self.rent_date:
            raise ValidationError("Return date cannot be before rent date.")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.vehicle.status = 'rented'
            self.vehicle.save()
        super().save(*args, **kwargs)
