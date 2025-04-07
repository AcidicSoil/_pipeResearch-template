# Code Documentation

## Inline Comments
- Dart code uses `///` for documentation comments
- Key areas include:
  - Custom Riverpod providers
  - LLM function handling logic
  - Sync manager for Drift <-> Supabase

## API Documentation
- **Tool:** Swagger/OpenAPI 3.1 via `supabase-openapi` plugin
- **Exposed Routes:**
  - `GET /tasks`, `POST /tasks`
  - `GET /calendar`, `POST /calendar`
  - `POST /assistant/fncall`
  - `POST /sync/tasks`, `POST /sync/calendar`
- Swagger JSON hosted on `/docs/swagger.json`
- Web UI via Swagger UI embedded at `/docs`

## Architecture Diagram
- MermaidJS-based flow diagrams (stored in `docs/user-flow.md`)
- Components:
  - Flutter UI
  - Riverpod State
  - Drift local DB
  - Supabase Edge Functions & Postgres
  - OpenAI LLM endpoint

## README
- Overview of app architecture
- Dev setup instructions
- Code structure & testing commands
- Deployment steps (Vercel + Supabase CLI)

## Documentation Standards

### Class Documentation

```dart
/// A service that handles authentication with Supabase.
///
/// This service manages user authentication state, session persistence,
/// and provides methods for login, signup, and account management.
///
/// Example:
/// ```dart
/// final authService = AuthService();
/// await authService.login('user@example.com', 'password');
/// ```
class AuthService {
  // Class implementation...
}
```

### Method Documentation

```dart
/// Creates a new task in the database.
///
/// Takes a [taskData] map containing the task details and persists it
/// to both local storage (Drift) and remote database (Supabase) if online.
///
/// Parameters:
/// - [taskData]: A map containing task properties (title, due date, etc.)
///
/// Returns:
/// A [Future<Task>] that completes with the created task including its ID.
///
/// Throws:
/// - [AuthException] if the user is not authenticated
/// - [ValidationException] if the task data is invalid
Future<Task> createTask(Map<String, dynamic> taskData) async {
  // Method implementation...
}
```

### File Headers

Each file should include a header comment that describes:
1. The purpose of the file
2. Key classes/functions contained
3. Related modules/files
4. Author and creation date

Example:
```dart
// task_repository.dart
//
// Repository for managing Task entities, providing methods for CRUD operations.
// Handles synchronization between local database (Drift) and remote (Supabase).
//
// Related files:
// - models/task.dart
// - database/task_dao.dart
//
// Created: 2023-10-15
```

### Commenting Conventions
- Use `TODO:` for planned improvements
- Use `FIXME:` for known bugs that need addressing
- Use `NOTE:` for important implementation details
- Group related code blocks with section comments