# Database Documentation

## Overview

This document outlines the database architecture, models, and access patterns used in the application. We use an in-memory database for development and testing, with a PostgreSQL implementation for production.

## Database Implementation

### Development/Testing

For development and testing, we use an `InMemoryDatabase` implementation with the following features:
- Table-based data organization
- CRUD operations
- Simple querying capabilities
- UUID-based ID generation
- Logging of database operations

### Production

For production, we use PostgreSQL with:
- Relational schema
- Indexed fields for performance
- Foreign key constraints
- Transaction support
- Connection pooling

## Core Data Models

### User
- **id**: UUID (primary key)
- **email**: String (unique)
- **password_hash**: String
- **name**: String
- **created_at**: Timestamp
- **settings**: JSON

### Task
- **id**: UUID (primary key)
- **user_id**: UUID (foreign key to User)
- **title**: String
- **description**: String (optional)
- **status**: Enum (todo, in_progress, completed)
- **priority**: Enum (low, medium, high)
- **due_date**: Timestamp (optional)
- **created_at**: Timestamp
- **updated_at**: Timestamp

### CalendarEvent
- **id**: UUID (primary key)
- **user_id**: UUID (foreign key to User)
- **title**: String
- **start_time**: Timestamp
- **end_time**: Timestamp
- **location**: String (optional)
- **description**: String (optional)
- **created_at**: Timestamp
- **updated_at**: Timestamp

### ChatMessage
- **id**: UUID (primary key)
- **user_id**: UUID (foreign key to User)
- **session_id**: UUID
- **content**: String
- **role**: Enum (user, assistant, system)
- **timestamp**: Timestamp

## Database Operations

### Common Patterns

```python
# Create a new item
item = db.insert("tasks", {
    "user_id": user_id,
    "title": "Complete project",
    "status": "todo",
    "priority": "high",
    "due_date": datetime.now() + timedelta(days=7)
})

# Retrieve an item by ID
task = db.get("tasks", task_id)

# Query items with a filter
overdue_tasks = db.query("tasks",
    lambda task: task["due_date"] < datetime.now() and task["status"] != "completed")

# Update an item
db.update("tasks", task_id, {**task, "status": "completed"})

# Delete an item
db.delete("tasks", task_id)
```

## Data Access Layer

The application uses a repository pattern to abstract database access:

```python
class TaskRepository:
    def __init__(self, db):
        self.db = db
        self.table_name = "tasks"

    def create(self, task_data):
        return self.db.insert(self.table_name, task_data)

    def get_by_id(self, task_id):
        return self.db.get(self.table_name, task_id)

    def get_by_user(self, user_id):
        return self.db.query(self.table_name,
            lambda task: task["user_id"] == user_id)

    # Additional methods...
```

## Performance Considerations

- Indexing on frequently queried fields
- Pagination for lists (limit/offset)
- Caching for repetitive queries
- Connection pooling for distributed load
- Optimized queries using database-specific features

## Security

- Parameterized queries to prevent SQL injection
- Row-level security for multi-tenant data
- Encrypted sensitive fields
- Connection encryption (TLS/SSL)