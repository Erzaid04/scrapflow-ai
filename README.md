# ScrapFlow AI

An AI-powered SaaS platform for scrap collectors, traders, and recycling businesses.

ScrapFlow AI is designed to digitize inventory management, transaction processing, supplier and buyer management, profitability tracking, and business operations through a secure, scalable backend architecture.

---

# Vision

Build a modern operating system for the scrap recycling industry by replacing manual record-keeping with intelligent, data-driven business management.

---

# Current Status

## ✅ Completed

### Backend Foundation

* FastAPI backend setup
* MySQL database integration
* SQLAlchemy ORM configuration
* Database session management
* Layered Architecture (Routes → Schemas → Services → Models)
* Dependency Injection

### Authentication & Authorization

* User Management
* Password Hashing (bcrypt)
* User Registration API
* User Login API
* JWT Authentication
* OAuth2 Integration
* Protected Routes
* Current User API
* Role-Based Access Control (RBAC)

### Inventory Management

* Inventory Model
* Inventory CRUD APIs
* Inventory Validation
* Inventory RBAC
* MySQL Persistence

### Transaction Management

* Purchase Transactions
* Sale Transactions
* Automatic Inventory Synchronization
* Stock Validation
* Transaction RBAC
* End-to-End API Testing

### Buyer Management

* Buyer Model
* Buyer CRUD Foundation
* Duplicate Phone Validation
* Buyer RBAC
* MySQL Persistence
* End-to-End API Testing

### Supplier Management

* Supplier Model
* Supplier CRUD Foundation
* Duplicate Phone Validation
* Supplier RBAC
* MySQL Persistence
* End-to-End API Testing

### Testing

* Swagger UI Testing
* Authentication Testing
* RBAC Testing
* Inventory Testing
* Transaction Testing
* Buyer Testing
* Supplier Testing

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

## Developer Tools

* Git
* GitHub
* Swagger UI

---

# Architecture

```text
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
```

---

# Implemented APIs

## Authentication

| Method | Endpoint              |
| ------ | --------------------- |
| POST   | /api/v1/auth/register |
| POST   | /api/v1/auth/login    |
| POST   | /api/v1/auth/token    |

---

## User

| Method | Endpoint         |
| ------ | ---------------- |
| GET    | /api/v1/users/me |

---

## Inventory

| Method | Endpoint               |
| ------ | ---------------------- |
| POST   | /api/v1/inventory      |
| GET    | /api/v1/inventory      |
| GET    | /api/v1/inventory/{id} |
| PUT    | /api/v1/inventory/{id} |
| DELETE | /api/v1/inventory/{id} |

---

## Transactions

| Method | Endpoint             |
| ------ | -------------------- |
| POST   | /api/v1/transactions |

---

## Buyers

| Method | Endpoint                  |
| ------ | ------------------------- |
| POST   | /api/v1/buyers            |
| GET    | /api/v1/buyers            |
| GET    | /api/v1/buyers/{buyer_id} |

---

## Suppliers

| Method | Endpoint                        |
| ------ | ------------------------------- |
| POST   | /api/v1/suppliers               |
| GET    | /api/v1/suppliers               |
| GET    | /api/v1/suppliers/{supplier_id} |

---

# User Roles

## Owner

* Full system access
* Inventory Management
* Transaction Management
* Buyer Management
* Supplier Management

---

## Worker

* Create Inventory
* Update Inventory
* Create Transactions
* Manage Buyers
* Manage Suppliers
* View Inventory

---

## Accountant

* View Inventory
* View Buyers
* View Suppliers
* View Business Data

---

# Business Rules

## Purchase Transactions

* Record purchase transaction
* Automatically increase inventory

## Sale Transactions

* Record sale transaction
* Automatically decrease inventory

## Inventory Validation

* Prevent negative inventory
* Prevent invalid inventory references

## Buyer Validation

* Prevent duplicate buyer phone numbers

## Supplier Validation

* Prevent duplicate supplier phone numbers

---

# Roadmap

## Phase 1 – Authentication & Authorization

* [x] User Registration
* [x] User Login
* [x] JWT Authentication
* [x] OAuth2
* [x] RBAC

---

## Phase 2 – Inventory Management

* [x] Inventory CRUD
* [x] Inventory Validation
* [x] Inventory RBAC

---

## Phase 3 – Transaction Management

* [x] Purchase Transactions
* [x] Sale Transactions
* [x] Inventory Synchronization
* [x] Stock Validation

---

## Phase 4 – Buyer Management

* [x] Buyer CRUD Foundation
* [x] Buyer Validation
* [x] Buyer RBAC

---

## Phase 5 – Supplier Management

* [x] Supplier CRUD Foundation
* [x] Supplier Validation
* [x] Supplier RBAC

---

## Phase 6 – Profit Engine

* [ ] Revenue Tracking
* [ ] Cost Tracking
* [ ] Profit Calculation
* [ ] Financial Analytics

---

## Phase 7 – Reporting & Dashboard

* [ ] Inventory Reports
* [ ] Buyer Reports
* [ ] Supplier Reports
* [ ] Profit Reports
* [ ] Business Dashboard

---

## Phase 8 – AI Features

* [ ] Scrap Price Prediction
* [ ] Demand Forecasting
* [ ] AI Business Assistant
* [ ] Smart Recommendations

---

# Project Structure

```text
backend/
├── app/
│   ├── auth/
│   ├── database/
│   ├── dependencies/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│
├── docs/
└── main.py
```

---

# Latest Milestone

Successfully implemented:

* Authentication System
* JWT Authentication
* OAuth2 Integration
* Role-Based Access Control (RBAC)
* Inventory Management Module
* Transaction Management Module
* Buyer Management Module
* Supplier Management Module
* Inventory Synchronization Engine
* Business Rule Validation
* Service Layer Architecture
* MySQL Integration
* Swagger API Testing

---

# Current Project Status

* ✅ Authentication System
* ✅ Authorization System
* ✅ JWT Authentication
* ✅ OAuth2 Integration
* ✅ RBAC System
* ✅ Inventory Management Module
* ✅ Transaction Management Module
* ✅ Buyer Management Module
* ✅ Supplier Management Module

## 🚀 Next Module

**Profit Engine**

---

## Author

**Zaid Hakim Kakar**

Backend Developer | Python | FastAPI | SQLAlchemy | MySQL
