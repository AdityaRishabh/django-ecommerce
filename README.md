
#  Installation & Setup

## 1 Clone Repository

```bash
git clone <your-repo-url>
cd authproject
```


## 2 Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  
```

---

## 3 Install Dependencies

```bash
pip install django djangorestframework psycopg2 python-dotenv djangorestframework-simplejwt
```

---

##  Create `.env` file

```
SECRET_KEY=your_secret_key

DB_NAME=authdb
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

##  Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

---

##  Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

---

##  Run Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```


#  Django E-Commerce Web Application

A full-featured **E-Commerce web application** built using Django.
This project supports both **web UI + REST APIs (Django REST Framework)** with **JWT Authentication**, 

#  Features

##  Authentication (Web + API)

* User Signup (Email-based)
* User Login (Email & Password)
* Logout functionality
* Session-based authentication (Web)
*  JWT Authentication (API)

  * Access Token
  * Refresh Token



# Product Management

* Product listing on dashboard
* Product images upload
* Product description & price
* Search functionality

# Product API (CRUD)

* GET all products
* POST (Add product - Admin only)
* PUT (Update product - Admin only)
* DELETE (Remove product - Admin only)


# Cart System

# Web Features

* Add to cart
* Increase / decrease quantity
* Remove items from cart
* Dynamic total calculation

###  Cart API (CRUD)

* GET user cart
* POST add to cart
* PATCH update quantity
* DELETE remove item


# Checkout (COD)

* Address & phone input
* Order placement (Cash on Delivery)
* Cart cleared after checkout


# Order Management

# Web

* Order history page
* Order detail view
* Order status tracking

# Order API

* GET user orders

# REST API Endpoints

# JWT Authentication

| Method | Endpoint              |
| ------ | --------------------- |
| POST   | `/api/token/`         |
| POST   | `/api/token/refresh/` |

---

# Products

| Method | Endpoint                    | Access |
| ------ | --------------------------- | ------ |
| GET    | `/api/products/`            | Public |
| POST   | `/api/add-product/`         | Admin  |
| PUT    | `/api/update-product/<id>/` | Admin  |
| DELETE | `/api/delete-product/<id>/` | Admin  |


# Cart

| Method | Endpoint                 |
| ------ | ------------------------ |
| GET    | `/api/cart/`             |
| POST   | `/api/add-to-cart/`      |
| PATCH  | `/api/update-cart/<id>/` |
| DELETE | `/api/remove-cart/<id>/` |



# Orders

| Method | Endpoint       |
| ------ | -------------- |
| GET    | `/api/orders/` |

---

#  JWT Authentication Usage (Postman)

## 1️ Get Token

```json
POST /api/token/
{
  "username": "your_username",
  "password": "your_password"
}
```

## 2️ Use Token

Add in headers:

Authorization: Bearer <access_token>


#  Tech Stack

* **Backend:** Django, Django REST Framework
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** PostgreSQL
* **Authentication:**

  * Django Auth (Session)
  * JWT (API)
* **Media Handling:** Image upload
* **Environment Variables:** python-dotenv


#  Application Flow

### Web Flow

1. User signs up / logs in
2. Dashboard shows products
3. User adds items to cart
4. Manages cart
5. Checkout (COD)
6. Order stored
7. View order history


### API Flow

1. Get JWT token
2. Use token in headers
3. Perform CRUD operations
4. Admin controls product APIs


#  Key Concepts Used

* Django ORM
* REST APIs (DRF)
* JWT Authentication
* Session vs Token Auth
* CRUD Operations
* ForeignKey relationships
* File/Image uploads
* Permissions (Admin vs User)


#  Security Features

* JWT Authentication (API)
* Password Hashing
* Role-based access (Admin/User)
* Environment variables for secrets


