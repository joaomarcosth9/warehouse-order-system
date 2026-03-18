# Order Management System (Clean Architecture & DDD)

A technical implementation of an Order Management System built with **FastAPI**, focusing on **Domain-Driven Design (DDD)** and **Hexagonal Architecture**.

Maybe a little over engineered for a simple assignment, but I preferred to do it that way, so it will be (maybe) easier to extend.

## Getting Started

This project uses [uv](https://astral.sh/uv/) for fast Python dependency management.

### 1. Install Dependencies
```bash
uv sync
```

### 2. Run the Application

```bash
make run
```

### 3. Run Lint + Type Check

```bash
make lint
```

The API will be available at `http://127.0.0.1:8000`.
Interactive documentation (Swagger UI) can be found at `/docs`.

---

## Usage Examples (CURL)

### 1. Create a Successful Order

This will automatically select the closest warehouse that has all items in stock.

```bash
curl -X POST http://localhost:8000/orders \
-H "Content-Type: application/json" \
-d '{
  "customer_id": "cust_123",
  "shipping_address": {
    "street": "123 Tech Ave",
    "city": "New York",
    "state": "NY",
    "zip_code": "10001"
  },
  "items": [
    {"product_id": "prod-1", "quantity": 2},
    {"product_id": "prod-2", "quantity": 1}
  ]
}'
```

### 2. Business Error: Out of Stock (HTTP 400)

```bash
curl -X POST http://localhost:8000/orders \
-H "Content-Type: application/json" \
-d '{
  "customer_id": "cust_123",
  "shipping_address": {"street": "Main St", "city": "Buffalo", "state": "NY", "zip_code": "14201"},
  "items": [{"product_id": "prod-1", "quantity": 99999}]
}'
```

### 3. Healthcheck

```bash
curl http://localhost:8000/
```
