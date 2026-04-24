# RentalPro: Complete Vehicle Rental System

A premium, modular Vehicle Rental System built with Django, following **Vibe Coding** principles. This system allows for efficient management of vehicles, customers, and rental transactions with a modern, responsive UI.

## 🚀 Features

- **Vehicle Management**: Full CRUD operations for vehicles with real-time status tracking (Available/Rented).
- **Customer Management**: Easy registration and directory of customers.
- **Rental System**: 
    - Intelligent rental processing.
    - Automatic validation (prevents renting already rented vehicles).
    - One-click vehicle return with automatic cost calculation.
    - Complete rental history tracking.
- **Premium UI**: Clean, modern dashboard with quick stats and smooth transitions.
- **Dockerized**: Fully containerized for one-command deployment.

## 🛠 Tech Stack

- **Backend**: Django 5.x
- **Frontend**: Django Templates, Bootstrap 5, Custom CSS (Vanilla)
- **Database**: SQLite3 (Clean and simple for local dev)
- **DevOps**: Docker, Docker Compose
- **Styling**: Google Fonts (Outfit), Bootstrap Icons

## 📂 Project Structure

```text
vehicle_rental_pro/
├── backend/
│   ├── rental_project/    # Django Project Settings
│   ├── rental_app/        # Core Application Logic
│   ├── templates/         # HTML Templates
│   ├── static/            # CSS and Assets
│   ├── manage.py
│   └── requirements.txt
├── Dockerfile             # Container definition
├── docker-compose.yml     # Orchestration
└── README.md
```

## ⚙️ Setup Instructions

### Option 1: Using Docker (Recommended)

1. Ensure you have Docker and Docker Compose installed.
2. Run the following command from the root directory:
   ```bash
   docker-compose up --build
   ```
3. The application will be available at `http://localhost:8000`.

### Option 2: Manual Setup

1. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. **Install Dependencies**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
3. **Run Migrations & Load Data**:
   ```bash
   python manage.py migrate
   python manage.py load_sample_data
   ```
4. **Start Server**:
   ```bash
   python manage.py runserver
   ```
5. Visit `http://127.0.0.1:8000`.

## 📸 Suggested Screenshots for Submission

1. **Dashboard**: High-level overview of inventory and recent activities.
2. **Vehicle Inventory**: Grid view showing available and rented vehicles.
3. **Rental Form**: Selecting a customer and dates for a specific vehicle.
4. **Rental History**: List of all past and active rentals with cost tracking.
5. **Django Admin**: Backend management interface.

---
Built with ❤️ using Django and Vibe Coding Principles.
