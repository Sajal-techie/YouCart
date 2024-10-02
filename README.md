# YouCart - E-Commerce Platform

YouCart is a full-featured eCommerce platform built using Django as the backend framework and includes features such as user registration, product management, shopping cart, order processing, and more. The platform provides a responsive and intuitive user interface for browsing products and managing orders.

## Features
- **User Authentication**: Secure registration and login functionality.
- **Product Management**: Admin can add, update, and delete products.
- **Shopping Cart**: Users can add products to the cart, update quantities, and proceed to checkout.
- **Order History**: Users can view their past orders and order details.
- **Responsive Design**: Optimized for both desktop and mobile devices.


## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap), Django Templates
- **Database**: SQLite3 (can be replaced with PostgreSQL or MySQL)
- **Authentication**: Django's built-in authentication with email-based verification


## Installation

To set up the project locally, follow these steps:

**1. Clone the repository**:
```
git clone https://github.com/Sajal-techie/YouCart.git
```
**2. Set up a virtual environment**:

```
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

**3. Install the required dependencies**:
```
pip install -r requirements.txt
```
**5. Run the migrations**:
```
python manage.py migrate
```
**6. Create a superuser for the admin dashboard**:
```
python manage.py createsuperuser
```
**7. Run the server**:
```
python manage.py runserver
```

Visit http://127.0.0.1:8000 to view the app.

**8. Access the Admin Dashboard**:
To access the admin panel, visit /admin_login/ and log in with the superuser credentials
