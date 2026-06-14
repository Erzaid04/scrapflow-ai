# ScrapFlow AI

AI-powered operating system for scrap collectors, traders, and recycling businesses.

## Vision

Digitize scrap collection, inventory tracking, sales management, profitability tracking, and business operations through a modern SaaS platform.

---

## Current Status

### Completed

* FastAPI backend setup
* MySQL database integration
* SQLAlchemy ORM setup
* Database session management
* User model implementation
* Password hashing with bcrypt
* User registration API
* User login API
* JWT authentication
* Token verification
* Swagger API documentation and testing

### In Progress

* Authorization system
* Protected routes
* Current user API

---

## Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* MySQL
* Pydantic
* JWT Authentication
* Passlib (bcrypt)

### Frontend (Planned)

* HTML
* CSS
* JavaScript

### Dev Tools

* Git
* GitHub
* Swagger UI

---

## Architecture

Frontend
↓
Routes
↓
Schemas
↓
Services
↓
Security / JWT
↓
Models
↓
Database

---

## Implemented APIs

### Authentication

#### Register User

POST /api/v1/auth/register

Features:

* Email validation
* Phone validation
* Password hashing
* User creation

#### Login User

POST /api/v1/auth/login

Features:

* Credential verification
* JWT token generation
* Bearer token authentication

---

## Roadmap

### Phase 1: Authentication & Authorization

* [x] User Registration
* [x] User Login
* [x] JWT Authentication
* [ ] Protected Routes
* [ ] Role-Based Access Control

### Phase 2: Inventory Management

* [ ] Inventory Tracking
* [ ] Material Categories
* [ ] Stock Management
* [ ] Batch Tracking

### Phase 3: Business Operations

* [ ] Sales Management
* [ ] Expense Tracking
* [ ] Collection Management
* [ ] Customer Management

### Phase 4: Analytics

* [ ] Reports Dashboard
* [ ] Profitability Analysis
* [ ] Business Insights

### Phase 5: AI Features

* [ ] AI Assistant
* [ ] Demand Forecasting
* [ ] Price Prediction
* [ ] Smart Recommendations

---

## Project Structure

backend/
├── app/
│ ├── auth/
│ ├── database/
│ ├── models/
│ ├── routes/
│ ├── schemas/
│ └── services/
├── docs/
└── main.py

---

## Latest Milestone

Successfully implemented a complete JWT-based authentication system with secure password hashing and bearer token authentication.
