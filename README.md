# ScrapFlow AI

AI-powered operating system for scrap collectors, traders, and recycling businesses.

---

# Vision

Digitize scrap collection, inventory management, supplier management, buyer management, purchase & sale transactions, profitability tracking, reporting, and business operations through a modern SaaS platform.

---

# Current Status

## Completed

### Backend Foundation

- FastAPI backend setup
- MySQL database integration
- SQLAlchemy ORM configuration
- Database session management
- Layered architecture implementation
- Service-oriented architecture
- Decimal-based financial calculations

---

## Authentication & Authorization

### Authentication

- User model implementation
- Password hashing with bcrypt
- User registration API
- User login API
- JWT authentication
- OAuth2 integration
- Protected routes
- Current user API

### Authorization

- Role-Based Access Control (RBAC)
- Owner permissions
- Worker permissions
- Accountant permissions
- Route-level authorization

---

## Inventory Management

- Inventory model
- Inventory CRUD APIs
- Inventory validation
- Inventory RBAC
- MySQL persistence
- Decimal precision for inventory quantity
- Purchase price tracking

---

## Buyer Management

- Buyer model
- Buyer CRUD foundation
- Buyer service layer
- Duplicate phone validation
- Buyer RBAC
- MySQL persistence
- End-to-end API testing

---

## Supplier Management

- Supplier model
- Supplier CRUD foundation
- Supplier service layer
- Duplicate phone validation
- Supplier RBAC
- MySQL persistence
- End-to-end API testing

---

## Transaction Management

### Purchase Transactions

- Purchase workflow
- Inventory synchronization
- Automatic stock updates
- Purchase transaction recording

### Sale Transactions

- Sale workflow
- Inventory synchronization
- Automatic stock deduction
- Stock validation
- Sale transaction recording

### Profit Engine

- Revenue calculation
- Cost calculation
- Profit calculation
- Purchase price snapshot
- Financial transaction recording
- Decimal-based financial precision

---

## Reporting

### Profit Summary API

- SQL aggregate reporting
- Total revenue calculation
- Total cost calculation
- Total profit calculation
- Empty database fallback
- Production-ready reporting service

---

## Testing

- Swagger API testing
- Authentication testing
- RBAC testing
- Inventory CRUD testing
- Buyer workflow testing
- Supplier workflow testing
- Purchase workflow testing
- Sale workflow testing
- Profit calculation testing
- Reporting API testing

---

# Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy ORM
- MySQL
- Pydantic
- JWT Authentication
- OAuth2
- Passlib (bcrypt)

---

## Frontend (Planned)

- HTML
- CSS
- JavaScript

---

## Dev Tools

- Git
- GitHub
- Swagger UI

---

# Architecture

```
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
Authentication / Authorization
        ↓
Models
        ↓
MySQL Database
```

---

# Implemented APIs

## Authentication APIs

### Register User

```
POST /api/v1/auth/register
```

### Login User

```
POST /api/v1/auth/login
```

### OAuth2 Token

```
POST /api/v1/auth/token
```

---

## User APIs

### Current User

```
GET /api/v1/users/me
```

---

## Inventory APIs

### Create Inventory

```
POST /api/v1/inventory
```

### Get All Inventory

```
GET /api/v1/inventory
```

### Get Inventory By ID

```
GET /api/v1/inventory/{id}
```

### Update Inventory

```
PUT /api/v1/inventory/{id}
```

### Delete Inventory

```
DELETE /api/v1/inventory/{id}
```

---

## Buyer APIs

### Create Buyer

```
POST /api/v1/buyers
```

### Get All Buyers

```
GET /api/v1/buyers
```

### Get Buyer By ID

```
GET /api/v1/buyers/{buyer_id}
```

---

## Supplier APIs

### Create Supplier

```
POST /api/v1/suppliers
```

### Get All Suppliers

```
GET /api/v1/suppliers
```

### Get Supplier By ID

```
GET /api/v1/suppliers/{supplier_id}
```

---

## Transaction APIs

### Create Transaction

```
POST /api/v1/transaction/transactions
```

### Features

- Purchase transactions
- Sale transactions
- Revenue calculation
- Cost calculation
- Profit calculation
- Inventory synchronization
- Stock validation

---

## Reporting APIs

### Profit Summary

```
GET /api/v1/reports/profit-summary
```

Returns

- Total Revenue
- Total Cost
- Total Profit

---

# Roles

## Owner

Permissions

- Full system access
- Manage inventory
- Manage buyers
- Manage suppliers
- Manage transactions
- View reports

---

## Worker

Permissions

- Create inventory
- Update inventory
- Create buyers
- Create suppliers
- Create transactions
- View inventory
- View buyers
- View suppliers

---

## Accountant

Permissions

- View inventory
- View buyers
- View suppliers
- View reports
- View financial data

Restrictions

- Cannot modify inventory
- Cannot create transactions

---

# Business Rules

## Purchase Transaction

When a purchase transaction is created

- Transaction is recorded
- Cost is calculated
- Inventory quantity increases automatically
- Purchase price snapshot is stored

---

## Sale Transaction

When a sale transaction is created

- Transaction is recorded
- Revenue is calculated
- Cost is calculated
- Profit is calculated automatically
- Inventory quantity decreases automatically

---

## Inventory Validation

The system prevents

- Negative inventory
- Selling unavailable stock
- Invalid inventory references

---

## Financial Rules

The system automatically calculates

- Revenue
- Cost
- Profit

All financial values use Decimal precision.

---

## Buyer Validation

The system prevents

- Duplicate phone numbers
- Invalid buyer references

---

## Supplier Validation

The system prevents

- Duplicate phone numbers
- Invalid supplier references

---

# Roadmap

## Phase 1 — Authentication & Authorization

- [x] User Registration
- [x] User Login
- [x] JWT Authentication
- [x] Protected Routes
- [x] Role-Based Access Control

---

## Phase 2 — Inventory Management

- [x] Inventory Create
- [x] Inventory List
- [x] Inventory By ID
- [x] Inventory Update
- [x] Inventory Delete
- [x] Inventory Validation

---

## Phase 3 — Business Management

### Buyers

- [x] Buyer Registration
- [x] Buyer APIs
- [x] Buyer Validation

### Suppliers

- [x] Supplier Registration
- [x] Supplier APIs
- [x] Supplier Validation

---

## Phase 4 — Transaction Engine

- [x] Purchase Transactions
- [x] Sale Transactions
- [x] Inventory Synchronization
- [x] Stock Validation
- [x] Purchase Price Snapshot

---

## Phase 5 — Profit Engine

- [x] Revenue Tracking
- [x] Cost Tracking
- [x] Profit Calculation
- [x] Financial Transaction Recording

---

## Phase 6 — Reporting

- [x] Profit Summary API

Planned

- [ ] Monthly Profit Report
- [ ] Inventory Report
- [ ] Buyer Report
- [ ] Expense Report

---

## Phase 7 — Expense Management

- [ ] Expense CRUD
- [ ] Expense Categories
- [ ] Expense Tracking
- [ ] Net Profit Calculation

---

## Phase 8 — Dashboard

- [ ] Dashboard Summary
- [ ] Revenue Metrics
- [ ] Expense Metrics
- [ ] Inventory Metrics
- [ ] Gross Profit
- [ ] Net Profit

---

## Phase 9 — AI Features

- [ ] AI Business Assistant
- [ ] Voice Notes
- [ ] Speech-to-Text
- [ ] Scrap Price Prediction
- [ ] Demand Forecasting
- [ ] Smart Recommendations

---

# Project Structure

```
backend/
│
├── app/
│   ├── auth/
│   ├── database/
│   ├── dependencies/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   └── utils/
│
├── docs/
├── main.py
│
└── requirements.txt
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Erzaid04/scrapflow-ai.git
```

## Navigate to Backend

```bash
cd scrapflow-ai/backend
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Run the Server

```bash
uvicorn main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# Latest Milestone

Successfully implemented

- Authentication System
- Authorization System
- JWT Authentication
- OAuth2 Integration
- Role-Based Access Control (RBAC)
- Inventory Management Module
- Buyer Management Module
- Supplier Management Module
- Purchase & Sale Transaction Engine
- Revenue Calculation Engine
- Cost Calculation Engine
- Profit Calculation Engine
- Profit Summary Reporting API
- Inventory Synchronization
- Business Rule Validation
- SQL Aggregate Reporting
- Decimal-based Financial Precision
- Swagger API Testing

Current platform supports secure multi-role access, inventory management, supplier management, buyer management, financial transaction processing, and business reporting.

---

# Current Project Status

| Module | Status |
|---------|--------|
| Backend Foundation | ✅ |
| Authentication | ✅ |
| Authorization | ✅ |
| RBAC | ✅ |
| Inventory | ✅ |
| Buyers | ✅ |
| Suppliers | ✅ |
| Transaction Engine | ✅ |
| Profit Engine | ✅ |
| Reporting (Phase 1) | ✅ |
| Expense Management | ⏳ |
| Dashboard | ⏳ |
| Advanced Reports | ⏳ |
| AI Features | ⏳ |

---

# License

This project is developed for educational and startup purposes as part of the **ScrapFlow AI** SaaS platform.