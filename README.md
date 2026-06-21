# ScrapFlow AI

AI-powered operating system for scrap collectors, traders, and recycling businesses.

## Vision

Digitize scrap collection, inventory tracking, sales management, profitability tracking, and business operations through a modern SaaS platform.

---

## Current Status

### Completed

• FastAPI backend setup
• MySQL database integration
• SQLAlchemy ORM setup
• Database session management
• User model implementation
• Password hashing with bcrypt
• User registration API
• User login API
• JWT authentication
• OAuth2 integration
• Protected routes
• Current user API
• Role-Based Access Control (RBAC)
• Inventory Management MVP
• Inventory Create API
• Inventory List API
• Swagger API testing




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

* Frontend
* ↓
* Routes
* ↓
* Schemas
* ↓
* Services
* ↓
* Security / JWT
* ↓
* Models
* ↓
* Database

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
* [x] Protected Routes
* [x] Role-Based Access Control

### Phase 2: Inventory Management

Phase 2: Inventory Management

* [x] Inventory Tracking
* [x] Inventory Create API
* [x] Inventory List API
* [x] Inventory Update API
* [x] Inventory Delete API
* [x] Inventory By ID API

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

# backend/
* ├── app/
* │ ├── auth/
* │ ├── database/
* │ ├── models/
* │ ├── routes/
* │ ├── schemas/
* │ └── services/
* ├── docs/
* └── main.py

---

## Latest Milestone

Successfully implemented a complete Authentication and Authorization system with JWT, OAuth2, Protected Routes, and Role-Based Access Control (RBAC).

Built the first business module (Inventory Management MVP) including inventory creation, inventory listing, MySQL persistence, and role-based permissions.

Current platform supports secure multi-role access for Owners, Workers, and Accountants.

