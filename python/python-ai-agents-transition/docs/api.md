# API Documentation

## Overview

This FastAPI application provides a RESTful API for managing tea inventory.

## Base URL

- **Development**: `http://localhost:8000`
- **Production**: `https://your-domain.com`

## Authentication

Currently, the API is open (no authentication required). In production, implement JWT authentication.

## Endpoints

### Root

#### GET /

Returns a welcome message.

**Response:**

```json
{
  "message": "Hello, FastAPI!"
}
```

### Teas

#### GET /teas/

Retrieve all teas.

**Response:**

```json
[
  {
    "id": 1,
    "name": "Green Tea",
    "description": "Healthy tea"
  }
]
```

#### POST /teas/

Create a new tea.

**Request Body:**

```json
{
  "name": "Green Tea",
  "description": "Healthy tea"
}
```

**Response:**

```json
{
  "id": 1,
  "name": "Green Tea",
  "description": "Healthy tea"
}
```

#### GET /teas/{tea_id}

Retrieve a specific tea by ID.

**Parameters:**

- `tea_id` (integer): The ID of the tea

**Response:**

```json
{
  "id": 1,
  "name": "Green Tea",
  "description": "Healthy tea"
}
```

**Error Response (404):**

```json
{
  "detail": "Tea not found"
}
```

#### DELETE /teas/{tea_id}

Delete a tea by ID.

**Parameters:**

- `tea_id` (integer): The ID of the tea

**Response:**

```json
{
  "id": 1,
  "name": "Green Tea",
  "description": "Healthy tea"
}
```

### External Data

#### GET /fastapi-docs

Fetch FastAPI documentation from the official website.

**Response:** HTML content from fastapi.tiangolo.com

## Error Handling

The API uses standard HTTP status codes:

- `200` - Success
- `404` - Not Found
- `422` - Validation Error
- `500` - Internal Server Error

## Rate Limiting

Currently, no rate limiting is implemented. Consider adding rate limiting for production.

## CORS

CORS is enabled for all origins in development. Configure appropriately for production.
