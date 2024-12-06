# AzubiShop API

AzubiShop is a Django-based API designed to support an e-commerce platform where users can browse and purchase products, leave reviews, and manage their orders. This API handles product details, user authentication, order management, and more.

## Features

- **User Authentication:** User registration, login, and JWT-based authentication.
- **Product Catalog:** Browse, filter, and search products.
- **Shopping Cart:** Add products to the shopping cart, update quantities, and remove items.
- **Swagger API Documentation:** Access API endpoints and documentation via Swagger.

## Technologies Used

- **Backend:** Django, Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Authentication:** JWT (JSON Web Token)
- **Caching:** Redis (optional for performance improvements)
- **Hosting:** Heroku (for deployment)
- **API Documentation:** Swagger
- **Others:** Gunicorn (WSGI HTTP Server), SQLite (for development)

## Getting Started

These instructions will help you set up and run the project locally.

### Prerequisites

Make sure you have the following installed:
- Python 3.10 or higher
- pip (Python package manager)
- PostgreSQL (if you are not using the SQLite development database)

### Clone the Repository

### Admin Dashboard Endpoints
- https://azubi-api-f33a9b794cdf.herokuapp.com/dashboard/

## API Endpoints
- https://azubi-api-f33a9b794cdf.herokuapp.com/api/v1/users/admin/register/
- https://azubi-api-f33a9b794cdf.herokuapp.com/api/v1/users/admin/login/
- https://azubi-api-f33a9b794cdf.herokuapp.com/api/v1/users/register/
- https://azubi-api-f33a9b794cdf.herokuapp.com/api/v1/users/login/

- https://azubi-api-f33a9b794cdf.herokuapp.com/api/v1/store/products/
- https://azubi-api-f33a9b794cdf.herokuapp.com/api/v1/store/cart/

## API Document (Swagger)
- https://azubi-api-f33a9b794cdf.herokuapp.com/swagger/

```bash
git clone https://github.com/yourusername/azubieshop.git
cd azubieshop
