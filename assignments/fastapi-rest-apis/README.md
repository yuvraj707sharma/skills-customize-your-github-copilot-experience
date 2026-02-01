# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build robust and efficient REST APIs using the FastAPI framework. You will create a complete API with multiple endpoints, request validation, and proper HTTP status codes while understanding core concepts of RESTful API design.

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI Project and Create Basic Endpoints

#### Description
Set up a new FastAPI project with virtual environment and create a basic API with GET and POST endpoints. You'll start by installing dependencies and implementing simple endpoints that return data and accept user input.

#### Requirements
Completed program should:

- Create a virtual environment and install FastAPI and Uvicorn
- Initialize a main FastAPI application with a root endpoint that returns a welcome message
- Implement a GET endpoint `/items/{item_id}` that returns item details
- Implement a POST endpoint `/items/` that accepts item data and returns the created item
- Run the application using Uvicorn and verify endpoints work with test requests

### 🛠️ Task 2: Add Data Validation and Request Models

#### Description
Enhance your API by implementing Pydantic models for request/response validation. This ensures data integrity and provides automatic API documentation with proper schema definitions.

#### Requirements
Completed program should:

- Define Pydantic models for request data (e.g., Item model with name, description, price fields)
- Implement request body validation in POST endpoints
- Add query parameters to GET endpoints with type hints
- Return properly typed responses using the models
- Test the API to ensure invalid data is rejected with appropriate error messages

### 🛠️ Task 3: Implement Advanced Features and Error Handling

#### Description
Build upon your API by adding more sophisticated features such as in-memory data storage, proper HTTP status codes, error handling, and multiple related endpoints.

#### Requirements
Completed program should:

- Implement an in-memory database (list or dictionary) to store created items
- Create GET `/items/` endpoint that returns all stored items
- Implement PUT `/items/{item_id}` and DELETE `/items/{item_id}` endpoints for updates and deletions
- Add proper HTTP status codes (200, 201, 404, 400) for different scenarios
- Include error handling with custom error responses for missing items or invalid operations
- Document the API with docstrings and FastAPI's automatic documentation endpoint (`/docs`)
