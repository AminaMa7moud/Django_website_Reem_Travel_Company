# Reem Travel

Reem Travel is a Django-based web application for managing travel bookings, including hotel reservations, one-day trips, and package deals. The platform provides a user-friendly interface for customers to explore and book travel services.

# Features

    1. Home Page:
       A visually appealing landing page introducing the platform.
    2. Hotel Management:
       View hotel details, room types, and reviews.
    3. Trip Management:
       Explore one-day trips and internal trips with detailed information.
    4. Package Deals:
       Book packages that include hotels and trips.
    5. Booking System:
       Book hotels, trips, and packages with ease.
    6. Contact Form:
       Customers can send inquiries via the contact page.
    7. Admin Panel:
       Manage hotels, trips, packages, and bookings.

# Installation

1. **Clone the repository**:
   git clone https://github.com/yourrepo/reem-travel.git
   cd reem-travel

2. **Create a virtual environment and activate it:**:
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate

3. **Install dependencies:**:
   pip install -r requirements.txt

4. **Apply migrations:**:
   python manage.py migrate

5. **Create a superuser:**:
   python manage.py createsuperuser

6. **Run the development server:**:
   python manage.py runserver

7. **Open the application in your browser:**:
   http://127.0.0.1:8000/home/

# Configuration

    Database:
        The project uses PostgreSQL by default. Update the database settings in reem_travel/settings.py if needed.
    Static Files:
        Place your static files in the static/ directory.
    Media Files:
        Uploads are stored in the static/images/ directory.

# Usage

    Admin Panel:
        Access the admin panel at /admin/ to manage hotels, trips, and bookings.
    Booking:
        Users can book hotels, trips, and packages from the respective pages.
    Contact:
        Users can send inquiries via the contact page.

# Technologies Used

    Backend:
        Django 5.1.6
    Frontend:
        Bootstrap 5, HTML, CSS
    Database:
        PostgreSQL (default)
    Other:
        Font Awesome for icons
