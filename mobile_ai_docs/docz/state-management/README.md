# State Management

## Local State (Component-Level)
- Managed using `Riverpod` (Flutter)
- Used for transient UI state: modals, active tabs, text input values

## Global State (App-Wide)
- Managed using `Riverpod` providers with `StateNotifier`
- Tracks core entities:
  - Authenticated user
  - Task list
  - Calendar events
  - Assistant chat history

## Server State (Sync & Caching)
- Handled via `Riverpod` + custom `Repository` classes
- Data fetched from Supabase REST endpoints and cached in memory
- Offline support:
  - Locally stored entities with Drift (SQLite)
  - Periodic sync with `/sync/tasks` and `/sync/calendar`

## Persistence
- Supabase session tokens stored via `flutter_secure_storage`
- App preferences stored via `shared_preferences`
- Tasks/events cached locally with Drift (for offline editing)

## Example Provider
```dart
final tasksProvider = StateNotifierProvider<TaskNotifier, List<Task>>((ref) {
  return TaskNotifier(taskRepository);
});
```

## Data Consistency Strategy
- Timestamps used for conflict resolution during sync
- LLM-triggered actions modify both local + cloud state
- Offline queue holds unsynced mutations and retries automatically

## State Organization

### Core Providers
- `authProvider`: Manages authentication state and user session
- `taskProvider`: Manages tasks with CRUD operations
- `calendarProvider`: Manages calendar events
- `chatProvider`: Manages AI assistant chat history and session

### UI State Providers
- `themeProvider`: Light/dark theme toggle
- `navigationProvider`: Current tab and navigation history
- `modalProvider`: Controls modal dialogs and their state

### Repository Providers
- `taskRepositoryProvider`: Handles task CRUD with backend
- `calendarRepositoryProvider`: Handles calendar event CRUD with backend
- `chatRepositoryProvider`: Handles chat history with backend

## State Update Flow

1. UI triggers action (e.g., user taps "Create Task")
2. Action dispatched to appropriate provider
3. Provider updates local state
4. Repository asynchronously syncs with backend
5. UI reactively updates based on state changes

## Best Practices

- Keep providers focused on specific domain concerns
- Use `family` modifiers for parameterized state
- Implement proper error handling in all providers
- Use `ref.watch` for reactive updates
- Use `ref.read` for one-time actions
- Separate UI state from domain state
- Test providers independently