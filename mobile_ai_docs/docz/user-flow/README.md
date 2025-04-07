# User Flow Diagram

```mermaid
flowchart TD

  Start([User Opens App]) --> CheckAuth{Is Logged In?}
  CheckAuth -- No --> Signup[Signup / Login Screen]
  Signup --> AuthSupabase[Authenticate with Supabase]
  AuthSupabase --> Onboarding[Initial Onboarding Flow]
  Onboarding --> MainNav

  CheckAuth -- Yes --> MainNav

  MainNav[[Main Dashboard]] --> Tabs{Select Tab}
  Tabs --> Tasks[Task Manager View]
  Tabs --> Calendar[Calendar View]
  Tabs --> Chat[AI Assistant Chat]

  %% Task Flow
  Tasks --> ViewTasks[View Task List]
  ViewTasks --> AddTask[Create Task]
  AddTask --> SaveTask[POST /tasks]
  ViewTasks --> EditTask[Edit Existing Task]
  EditTask --> UpdateTask[PUT /tasks/:id]
  ViewTasks --> DeleteTask[Delete Task]
  DeleteTask --> Remove[DELETE /tasks/:id]

  %% Calendar Flow
  Calendar --> ViewEvents[View Events]
  ViewEvents --> AddEvent[Create Event]
  AddEvent --> SaveEvent[POST /calendar]
  ViewEvents --> DeleteEvent[Delete Event]
  DeleteEvent --> RemoveEvent[DELETE /calendar/:id]

  %% Chat Flow
  Chat --> UserPrompt[User Sends Prompt]
  UserPrompt --> LLMReply[Assistant Response (phi3-mini)]
  LLMReply --> FuncCall{LLM Triggers Action?}
  FuncCall -- Yes --> TaskInsert[Create Task via AI]
  FuncCall -- No --> StayChat[Stay in Chat]

  %% Sync + Offline
  MainNav --> SyncEngine[Check Sync (Drift/Server)]
  SyncEngine --> ConflictCheck{Conflicts Exist?}
  ConflictCheck -- Yes --> ResolvePrompt[Prompt User or Overwrite]
  ConflictCheck -- No --> ContinueUse[Continue Use]

  %% Errors
  AnyError[[Any API Error]] --> ShowToast[Show Error Message / Retry Option]

  %% Notifications
  Assistant --> ReminderCheck[Background Reminder Trigger]
  ReminderCheck --> PushNote[Push Notification to User]

  %% Logout
  MainNav --> Logout[Logout Button]
  Logout --> ConfirmLogout --> BackToLogin[Go to Login Screen]
```

## Flow Descriptions

### Authentication Flow
1. User opens app
2. App checks if user is logged in
3. If not logged in, show signup/login screen
4. User authenticates via Supabase
5. First-time users go through onboarding
6. Returning users go directly to main dashboard

### Task Management Flow
1. User selects Task tab in main navigation
2. User views list of tasks
3. User can create new task, which sends POST request to API
4. User can edit existing task, which sends PUT request to API
5. User can delete task, which sends DELETE request to API

### Calendar Management Flow
1. User selects Calendar tab in main navigation
2. User views calendar events
3. User can create new event, which sends POST request to API
4. User can delete event, which sends DELETE request to API

### AI Assistant Flow
1. User selects Chat tab in main navigation
2. User sends text prompt to assistant
3. Assistant (powered by phi3-mini) sends response
4. If LLM response triggers action (e.g., "create a task"), app performs action
5. Otherwise, conversation continues in chat interface

### Sync & Offline Flow
1. App periodically checks for sync changes
2. If conflicts exist between local and server data, prompt user or apply policy
3. If no conflicts, continue normal operation

### Error Handling
1. When API errors occur, show error toast message
2. Provide retry option where appropriate

### Notifications
1. Assistant can trigger background reminders
2. Reminders generate push notifications to user

### Logout Flow
1. User can logout from main navigation
2. Confirmation dialog shown
3. After logout, return to login screen