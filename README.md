# E-Commerce-Full-Stack-Project
Django, React, PostgreSQL, CORS,  

-- Full E-Commerce Architecture (Frontend + Backend)
-- Django Backend with REST APIs
-- React Frontend with modern UI
-- Product Listing & Product Details
-- User Authentication (Login / Signup)
-- Add to Cart Functionality
-- Order Placement Flow
-- API Integration (React ↔ Django)
-- State Handling in React
-- Secure Data Flow & Validation
-- Real-world folder structure

### Backend (Django)
-- Django Project Setup
-- Models & ORM
-- REST API Creation
-- Serializers & Views
-- Authentication Logic
-- Cart & Order APIs
-- Database Design for E-Commerce

### Frontend (React)
-- React Project Setup
-- Component-based Architecture
-- API Calling & Data Rendering
-- Product UI & Reusability
-- State Management Basics
-- Cart UI Logic
-- Connecting React with Django APIs

---
#### Day-01
---
## Backend Setup
```
pip install django djangorestframework psycopg2-binary python-dotenv
```
```
django-admin startproject backend .   [PROJECT]
```
```
python manage.py startapp store  [APP]
```
## Frontend Setup
```
pip install npm
```
```
npm create vite@latest
```
## DataBase
```
psql -U postgres
```
if above not working Then,

```
Windows key → type SQL Shell (psql) → Open
```
```
enter 4 to 5 times
```
we will get
```
postgres=#
```
then
```
CREATE DATABASE ecommerce_db;
```
```
\l
```
```
\q
```
```
python manage.py migrate
```

### Now,More about Project
```
python manage.py createsuperuser
```
```
Username:      admin
Email address: nagarajloni123@gmail.com
Password:      admin
```
## Run Application Now:
```
python manage.py runserver
```
```
http://127.0.0.1:8000/
```

---
#### Day-02
---

