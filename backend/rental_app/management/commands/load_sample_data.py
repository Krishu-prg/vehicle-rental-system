from django.core.management.base import BaseCommand
from rental_app.models import Vehicle, Customer

class Command(BaseCommand):
    help = 'Loads sample vehicles and customers'

    def handle(self, *args, **kwargs):
        # Sample Vehicles
        vehicles = [
            {'name': 'Tesla Model 3', 'vehicle_type': 'car', 'price_per_day': 150, 'image_url': 'https://images.unsplash.com/photo-1560958089-b8a1929cea89?q=80&w=2071&auto=format&fit=crop'},
            {'name': 'Harley Davidson Iron 883', 'vehicle_type': 'bike', 'price_per_day': 80, 'image_url': 'https://images.unsplash.com/photo-1558981403-c5f9899a28bc?q=80&w=2070&auto=format&fit=crop'},
            {'name': 'Ford F-150', 'vehicle_type': 'truck', 'price_per_day': 120, 'image_url': 'https://images.unsplash.com/photo-1583121274602-3e2820c69888?q=80&w=2070&auto=format&fit=crop'},
            {'name': 'Toyota Land Cruiser', 'vehicle_type': 'suv', 'price_per_day': 200, 'image_url': 'https://images.unsplash.com/photo-1550522105-0925902bc924?q=80&w=2070&auto=format&fit=crop'},
        ]

        for v_data in vehicles:
            Vehicle.objects.get_or_create(name=v_data['name'], defaults=v_data)
        
        # Sample Customers
        customers = [
            {'name': 'John Doe', 'email': 'john@example.com', 'phone': '9876543210', 'address': '123 Main St, NY'},
            {'name': 'Jane Smith', 'email': 'jane@example.com', 'phone': '9876543211', 'address': '456 Elm St, CA'},
        ]

        for c_data in customers:
            Customer.objects.get_or_create(email=c_data['email'], defaults=c_data)

        self.stdout.write(self.style.SUCCESS('Successfully loaded sample data'))
