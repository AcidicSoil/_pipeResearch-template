# API Documentation

## General
- **Base URL (Supabase Edge Functions):** `https://yourproject.supabase.co/functions/v1`
- **Auth:** Supabase JWT via client SDK or Bearer token
- **Response format:** JSON

---

## 🔐 Auth Endpoints (Handled by Supabase Auth)
- `/auth/signup`
- `/auth/login`
- `/auth/logout`
- `/auth/user` – Fetch current user profile

---

## ✅ Task Endpoints

### `GET /tasks`
- **Desc:** Fetch all tasks for the authenticated user
- **Query Params:** `status`, `priority`, `due_before`, `updated_since`

### `POST /tasks`
- **Desc:** Create a new task
- **Body:**
```json
{
  "title": "Buy milk",
  "description": "Almond only",
  "priority": "medium",
  "status": "todo",
  "due_date": "2024-04-10T10:00:00Z",
  "source_type": "manual"
}
```

### `PUT /tasks/:id`
- **Desc:** Update an existing task
- **Body:** Partial or full task update

### `DELETE /tasks/:id`
- **Desc:** Delete a task

---

## 📅 Calendar Endpoints

### `GET /calendar`
- **Desc:** Get upcoming events
- **Query:** `range_start`, `range_end`

### `POST /calendar`
- **Desc:** Add new event manually or via LLM
- **Body:**
```json
{
  "title": "Doctor Appt",
  "start_time": "2024-04-12T14:00:00Z",
  "end_time": "2024-04-12T15:00:00Z",
  "location": "Clinic",
  "source": "llm"
}
```

### `DELETE /calendar/:id`
- **Desc:** Delete an event

---

## 💬 Chat Endpoints

### `POST /chat`
- **Desc:** Send user prompt to assistant
- **Body:**
```json
{
  "session_id": "abc-123",
  "message": "What do I have this week?",
  "model": "phi3-mini",
  "mode": "calendar"
}
```
- **Response:** Assistant message reply + function triggers (if applicable)

---

## 🤖 Model Management

### `GET /models`
- **Desc:** Get available assistant models and their metadata

### `POST /settings/assistant`
- **Desc:** Update user preferences (model, style, voice, fallback)

---

## Sync Utilities

### `GET /sync/tasks`
- **Query:** `updated_since`
- **Use:** Fetch only updated tasks for mobile sync

### `POST /sync/bulk`
- **Desc:** Upload batch of offline-edited tasks/messages
- **Conflict Strategy:** `last-write-wins` or prompt user

---

## Error Format
```json
{
  "error": true,
  "code": 401,
  "message": "Unauthorized"
}
```

---

## Rate Limits
- **Free Tier:** 60 RPM per endpoint
- **Pro Tier:** 200 RPM
- **Backoff header:** `Retry-After`

---

## Realtime (Optional)
- **Supabase Realtime Channels** (enabled on `tasks`, `chat_messages`, `calendar_events`)