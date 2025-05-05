# Chivent

Chivent-ticcketing_system is a Django-based e-commerce event ticketing web application prototype. It features user registration, a session-based shopping cart, multistep checkout with a mock payment flow, and a robust admin interface.

## Features

* **Catalog View**: Browse upcoming events with image, title, date/time, location, price, and available tickets
* **Event Detail**: Detailed page for each event
* **User Accounts**: Custom authentication system (registration/login)
* **Shopping Cart**: Session-based cart with quantity selection
* **Checkout Flow**: Reserve tickets, mock payment page, and confirmation
* **Orders**: Persistent orders with line-items, manageable in Django Admin
* **Admin Interface**: Manage events, users, and orders

## Prerequisites

* Python 3.8+
* pip
* MySQL server
* Git

## Local Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/chivent.git
   cd chivent
   ```
2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables**
   Create a `.env` file in the project root with:

   ```ini
   SECRET_KEY=your-django-secret-key
   DEBUG=True
   DB_NAME=chivent_dev
   DB_USER=chivent
   DB_PASSWORD=123
   DB_HOST=127.0.0.1
   DB_PORT=3306
   ```
5. **Set up the MySQL database**

   ```sql
   CREATE DATABASE chivent_dev CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
6. **Apply migrations**

   ```bash
   python manage.py migrate
   ```
7. **(Optional) Load fixtures**

   ```bash
   python manage.py loaddata fixtures/admin.json
   ```
8. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```
9. **Collect static files**

   ```bash
   python manage.py collectstatic
   ```
10. **Run the development server**

    ```bash
    python manage.py runserver
    ```
11. **Access the application**

    * **Frontend**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    * **Admin**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)


## Remote Demo

To gain access to my own remote demo that is deployed on render.com, please visit

[https://chivent-ticketing-dev.onrender.com](https://chivent-ticketing-dev.onrender.com)