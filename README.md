# Backend Take-Home: Orders API

Welcome! This is a small, scoped exercise meant to take **30-60 minutes**. We're not
looking for a polished production system — we're looking at how you think about
APIs, data validation, and working with a database.

## The scenario

You're building a tiny service that accepts orders, stores them, and lets you query
them back out.

## What you need to build

A Python server (any framework you like) running on **port 3000** with these four
endpoints:

### 1. `POST /orders`

Create a new order. Request body:

```json
{
  "customer_email": "person@example.com",
  "amount": 42.50,
  "status": "pending"
}
```

- `customer_email` (string, required)
- `amount` (positive number, required)
- `status` (string, optional — defaults to `"pending"`)

Respond with **201** and the stored order (including `id` and `created_at`):
```json
{
  "id": 1,
  "customer_email": "person@example.com",
  "amount": 42.50,
  "status": "pending",
  "created_at": "2026-07-13T12:00:00"
}
```

Respond **400** with `{ "error": "..." }` for invalid payloads.

### 2. `GET /orders`

Return all stored orders as a JSON array.

- Supports optional `?status=` query param to filter
- Always returns **200** (empty array if nothing matches)

### 3. `GET /orders/<id>`

Return a single order by its `id`.

- **200** with the order if found
- **404** with `{ "error": "not found" }` if not

### 4. `PATCH /orders/<id>`

Update an order's status. Request body:

```json
{
  "status": "shipped"
}
```

- `status` is the only field that can be updated
- **200** with the updated order
- **400** with `{ "error": "..." }` if `status` is missing or invalid
- **404** with `{ "error": "not found" }` if the order doesn't exist

## Database

Use **SQLite** (via `sqlite3` from the standard library or any ORM you prefer).
Your database should reset on each server restart — don't worry about persistence
across runs.

Your `orders` table should have at minimum:
- `id` — integer, primary key, auto-increment
- `customer_email` — text, not null
- `amount` — real, not null
- `status` — text, not null, default `"pending"`
- `created_at` — text, not null

## Getting started

```bash
# Pick your framework, e.g.:
pip install flask    # or fastapi, or use the stdlib http.server

# Run your server
python app.py        # or whatever you call it

# Test it manually
curl http://localhost:3000/orders
```

## What we're looking for

- Does it work? (test suite passing is the baseline)
- Is the validation sensible and not just hacked to pass specific tests?
- Is the code readable — would a teammate understand it?
