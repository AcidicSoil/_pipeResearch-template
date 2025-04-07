# Backend Documentation

## Overview

The backend supports a privacy-conscious AI assistant for mobile platforms. It handles user authentication, task and event management, voice/text interaction routing, and LLM integration. Designed with mobile-first principles, it ensures fast response times, hybrid reasoning, and local fallback.

---

## Tech Stack

- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL
- **Auth**: JWT (email/password)
- **API Style**: RESTful
- **Model Serving**:
  - Cloud/Hybrid: MLC LLM or vLLM
  - On-device fallback: llama.cpp
- **Speech Processing**: Whisper.cpp (offline STT)

---

## Core Features

### 1. User Management
- **POST /auth/register** – Create account
- **POST /auth/login** – Authenticate and return JWT
- **GET /auth/me** – Fetch current user profile
- **DELETE /auth/logout** – Invalidate token (client-side)

### 2. Tasks & Calendar
- **GET /tasks** – List all user tasks
- **POST /tasks** – Create a task (NLP + manual fields)
- **PUT /tasks/{id}** – Update task
- **DELETE /tasks/{id}** – Delete task
- **GET /calendar/events** – List calendar items
- **POST /calendar/events** – Add new event (natural language supported)
- **POST /calendar/parse** – NLP → structured event creation

### 3. Conversational Assistant
- **POST /chat** – Send message to LLM
- **POST /summarize** – Summarize text (emails, tasks, etc.)
- **POST /reason** – Hybrid routing for reasoning tasks
  - Detects context (local or cloud)
  - Returns streamed or batch response

### 4. Voice Interaction
- **POST /voice/transcribe** – STT using Whisper.cpp
- **POST /voice/command** – Converts transcription to LLM command

### 5. Preferences & Personalization
- **GET /settings** – Fetch personalization config
- **PUT /settings** – Update preferences
- Options:
  - Model privacy level
  - User goals (prioritize work, health, etc.)
  - Custom trigger words or prompt tone

### 6. Privacy & Syncing
- Local vs cloud LLM toggle
- Metadata stored only if user consents
- Device-specific sync tokens for multi-device usage

---

## Background Jobs
- Cron-based summarization of daily events
- Notification triggers
- Periodic updates to local model cache

---

## Error Handling
- Standardized error schema
- Custom FastAPI Exception Handlers:
  - Auth errors
  - Model routing errors
  - NLP parser fallback

---

## Security
- JWT-based route guards
- Field validation via Pydantic
- Rate-limiting on LLM endpoints
- Optional homomorphic encryption module for PII fields