# ScrapFlow AI

AI-powered operating system for scrap collectors, traders, and recycling businesses.

## Vision

Digitize scrap collection, inventory tracking, transaction management, buyer management, profitability tracking, and business operations through a modern SaaS platform.

---

# Current Status

## Completed

### Backend Foundation

* FastAPI backend setup
* MySQL database integration
* SQLAlchemy ORM configuration
* Database session management
* Layered architecture implementation

### Authentication & Authorization

* User model implementation
* Password hashing with bcrypt
* User registration API
* User login API
* JWT authentication
* OAuth2 integration
* Protected routes
* Current user API
* Role-Based Access Control (RBAC)

### Inventory Management

* Inventory model
* Inventory CRUD APIs
* Inventory RBAC
* Inventory validation
* MySQL persistence

### Transaction Management

* Transaction model
* Purchase transactions
* Sale transactions
* Inventory synchronization
* Automatic stock updates
* Inventory validation
* Transaction RBAC
* End-to-end API testing

### Buyer Management

* Buyer model
* Buyer APIs
* Buyer service layer
* Buyer validation
* Duplicate phone prevention
* Buyer RBAC
* MySQL persistence
* End-to-end API testing

### Testing

* Swagger API testing
* Authentication testing
* RBAC testing
* Inventory CRUD testing
* Transaction workflow testing
* Buyer workflow testing

---

# Tech Stack

## Backend

* Python
* FastAPI
* SQLAlchemy
* MySQL
* Pydantic
* JWT Authentication
* OAuth2
* Passlib (bcrypt)

## Frontend (Planned)

* HTML
* CSS
* JavaScript

## Dev Tools

* Git
* GitHub
* Swagger UI

---

# Architecture

Frontend
↓
Routes
↓
Schemas
↓
Services
↓
Dependencies
↓
Security / JWT
↓
Models
↓
Database

---

# Implemented APIs

## Authentication APIs

### Register User

POST /api/v1/auth/register

### Login User

POST /api/v1/auth/login

### OAuth2 Token

POST /api/v1/auth/token

---

## User APIs

### Current User

GET /api/v1/users/me

---

## Inventory APIs

### Create Inventory

POST /api/v1/inventory

### View Inventory

GET /api/v1/inventory

### View Inventory By ID

GET /api/v1/inventory/{id}

### Update Inventory

PUT /api/v1/inventory/{id}

### Delete Inventory

DELETE /api/v1/inventory/{id}

---

## Transaction APIs

### Create Transaction

POST /api/v1/transactions

Features:

* Purchase transactions
* Sale transactions
* Inventory synchronization
* Stock validation

---

## Buyer APIs

### Create Buyer

POST /api/v1/buyers

### Get All Buyers

GET /api/v1/buyers

### Get Buyer By ID

GET /api/v1/buyers/{buyer_id}

---

# Roles

## Owner

Permissions:

* Manage inventory
* Manage transactions
* Manage buyers
* Full system access

---

## Worker

Permissions:

* Create inventory
* Update inventory
* Create transactions
* Create buyers
* View inventory
* View buyers

---

## Accountant

Permissions:

* View inventory
* View buyers
* View business data
* Restricted from inventory modifications
* Restricted from transaction creation

---

# Business Rules

## Purchase Transaction

When a purchase transaction is created:

* Transaction is recorded
* Inventory quantity increases automatically

---

## Sale Transaction

When a sale transaction is created:

* Transaction is recorded
* Inventory quantity decreases automatically

---

## Inventory Validation

The system prevents:

* Negative inventory
* Selling unavailable stock
* Invalid inventory references

---

## Buyer Validation

The system prevents:

* Duplicate phone numbers
* Invalid buyer references

---

# Roadmap

## Phase 1: Authentication & Authorization

* [x] User Registration
* [x] User Login
* [x] JWT Authentication
* [x] Protected Routes
* [x] Role-Based Access Control

---

## Phase 2: Inventory Management

* [x] Inventory Create API
* [x] Inventory List API
* [x] Inventory By ID API
* [x] Inventory Update API
* [x] Inventory Delete API

---

## Phase 3: Transaction Management

* [x] Purchase Transactions
* [x] Sale Transactions
* [x] Inventory Synchronization
* [x] Stock Validation
* [x] Transaction RBAC

---

## Phase 4: Buyer Management

* [x] Buyer Registration
* [x] Buyer Search
* [x] Buyer History Foundation
* [x] Buyer APIs
* [x] Buyer RBAC

---

## Phase 5: Profit Engine

* [ ] Revenue Tracking
* [ ] Cost Tracking
* [ ] Profit Calculation
* [ ] Financial Insights

---

## Phase 6: Reporting & Dashboard

* [ ] Inventory Reports
* [ ] Transaction Reports
* [ ] Buyer Reports
* [ ] Profit Reports
* [ ] Business Dashboard

---

## Phase 7: AI Features

* [ ] AI Business Assistant
* [ ] Scrap Price Prediction
* [ ] Demand Forecasting
* [ ] Smart Recommendations

---

# Project Structure

backend/
├── app/
│
├── auth/
├── database/
├── dependencies/
├── models/
├── routes/
├── schemas/
├── services/
│
├── docs/
└── main.py

---

# Latest Milestone

Successfully implemented:

* Authentication System
* Authorization System
* JWT Authentication
* OAuth2 Integration
* Role-Based Access Control (RBAC)
* Inventory CRUD Module
* Transaction Management Module
* Buyer Management Module
* Inventory Synchronization Engine
* Business Rule Validation
* Swagger API Testing

Current platform supports secure multi-role access for Owners, Workers, and Accountants with inventory management, transaction processing, and buyer management workflows.

---

# Current Project Status

Authentication System: ✅ Completed

Authorization System: ✅ Completed

RBAC System: ✅ Completed

Inventory CRUD Module: ✅ Completed

Transaction Management Module: ✅ Completed

Buyer Management Module: ✅ Completed

Next Module: 🚀 Profit Engine
