#!/usr/bin/env python3
"""
AI Secretary API Server
----------------------
This module implements the FastAPI server for the AI Secretary mobile app,
providing endpoints for conversation, task management, calendar events, and email processing.
"""

import os
import json
import uuid
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta

import uvicorn
from fastapi import FastAPI, HTTPException, Depends, Body, Query, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Import LangGraph components
from langchain.schema import HumanMessage, AIMessage
from secretary_graph import (
    create_workflow,
    initialize_state,
    IntentionType,
    TaskPriority,
    Task,
    CalendarEvent,
    EmailSummary
)

# Load environment variables
load_dotenv()

# Initialize the app
app = FastAPI(
    title="AI Secretary API",
    description="Backend API for the AI Secretary mobile application",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create the workflow
secretary_workflow = create_workflow()

# In-memory session storage (replace with proper database in production)
user_sessions = {}

# Request and response models
class MessageRequest(BaseModel):
    text: str = Field(..., description="User message text")
    voice_data: Optional[str] = Field(None, description="Base64 encoded voice data")

class MessageResponse(BaseModel):
    text: str = Field(..., description="AI response text")
    voice_required: bool = Field(False, description="Whether voice response is needed")
    intention: str = Field(..., description="Detected user intention")

class TaskModel(BaseModel):
    id: str = Field(..., description="Task ID")
    title: str = Field(..., description="Task title")
    description: Optional[str] = Field(None, description="Task description")
    due_date: Optional[datetime] = Field(None, description="Task due date")
    priority: str = Field(..., description="Task priority (high/medium/low)")
    completed: bool = Field(False, description="Task completion status")
    created_at: datetime = Field(..., description="Task creation timestamp")

class CalendarEventModel(BaseModel):
    id: str = Field(..., description="Event ID")
    title: str = Field(..., description="Event title")
    description: Optional[str] = Field(None, description="Event description")
    start_time: datetime = Field(..., description="Event start time")
    end_time: datetime = Field(..., description="Event end time")
    location: Optional[str] = Field(None, description="Event location")
    participants: Optional[List[str]] = Field(None, description="Event participants")
    created_at: datetime = Field(..., description="Event creation timestamp")

class EmailSummaryModel(BaseModel):
    id: str = Field(..., description="Email ID")
    sender: str = Field(..., description="Email sender")
    subject: str = Field(..., description="Email subject")
    summary: str = Field(..., description="Email summary")
    received_at: datetime = Field(..., description="Email received timestamp")
    action_items: List[str] = Field(..., description="Action items from email")
    importance: str = Field(..., description="Email importance level")

# Session management
def get_or_create_session(user_id: str = Header(..., description="User ID for session management")):
    """
    Get or create a user session based on the user ID.
    """
    if user_id not in user_sessions:
        # Initialize a new session
        user_sessions[user_id] = {
            "state": initialize_state(),
            "created_at": datetime.now(),
            "last_activity": datetime.now(),
        }
    else:
        # Update last activity timestamp
        user_sessions[user_id]["last_activity"] = datetime.now()

    return user_sessions[user_id]

# API routes
@app.get("/")
async def root():
    """API health check endpoint."""
    return {"status": "healthy", "service": "AI Secretary API"}

@app.post("/api/conversation", response_model=MessageResponse)
async def converse(
    message: MessageRequest,
    session: Dict = Depends(get_or_create_session)
):
    """
    Process a user message and return the AI Secretary response.
    """
    try:
        # Get current state
        state = session["state"]

        # Add the user message to the state
        state["messages"].append(HumanMessage(content=message.text))

        # Process with LangGraph workflow
        config = {"configurable": {"thread_id": "user_session"}}
        result = secretary_workflow.invoke(state, config=config)

        # Update session state
        session["state"] = result

        # Get the AI response
        ai_messages = [msg for msg in result["messages"] if isinstance(msg, AIMessage)]
        if not ai_messages:
            raise HTTPException(status_code=500, detail="Failed to generate AI response")

        latest_response = ai_messages[-1].content

        # Determine if voice response should be generated
        # This is a simplified heuristic - in production, use more sophisticated logic
        voice_required = len(latest_response) < 100  # Only voice short responses

        return MessageResponse(
            text=latest_response,
            voice_required=voice_required,
            intention=result["intention"]
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing message: {str(e)}")

@app.get("/api/tasks", response_model=List[TaskModel])
async def get_tasks(
    session: Dict = Depends(get_or_create_session),
    completed: Optional[bool] = Query(None, description="Filter by completion status")
):
    """
    Get all tasks for the current user, optionally filtered by completion status.
    """
    tasks = session["state"]["tasks"]

    if completed is not None:
        tasks = [task for task in tasks if task["completed"] == completed]

    return tasks

@app.post("/api/tasks", response_model=TaskModel)
async def create_task(
    task_data: Dict[str, Any] = Body(...),
    session: Dict = Depends(get_or_create_session)
):
    """
    Manually create a new task.
    """
    task_id = str(uuid.uuid4())

    new_task = {
        "id": task_id,
        "title": task_data.get("title", "Untitled Task"),
        "description": task_data.get("description"),
        "due_date": datetime.fromisoformat(task_data.get("due_date")) if task_data.get("due_date") else None,
        "priority": task_data.get("priority", TaskPriority.MEDIUM),
        "completed": task_data.get("completed", False),
        "created_at": datetime.now()
    }

    session["state"]["tasks"].append(new_task)

    return new_task

@app.put("/api/tasks/{task_id}", response_model=TaskModel)
async def update_task(
    task_id: str,
    task_data: Dict[str, Any] = Body(...),
    session: Dict = Depends(get_or_create_session)
):
    """
    Update an existing task.
    """
    tasks = session["state"]["tasks"]

    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            # Update task fields
            tasks[i]["title"] = task_data.get("title", tasks[i]["title"])
            tasks[i]["description"] = task_data.get("description", tasks[i]["description"])

            if "due_date" in task_data and task_data["due_date"]:
                tasks[i]["due_date"] = datetime.fromisoformat(task_data["due_date"])

            tasks[i]["priority"] = task_data.get("priority", tasks[i]["priority"])
            tasks[i]["completed"] = task_data.get("completed", tasks[i]["completed"])

            return tasks[i]

    raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")

@app.get("/api/calendar", response_model=List[CalendarEventModel])
async def get_calendar_events(
    session: Dict = Depends(get_or_create_session),
    start_date: Optional[str] = Query(None, description="Filter by start date (ISO format)"),
    end_date: Optional[str] = Query(None, description="Filter by end date (ISO format)")
):
    """
    Get calendar events for the current user, optionally filtered by date range.
    """
    events = session["state"]["calendar_events"]

    # Apply date filters if provided
    if start_date:
        start = datetime.fromisoformat(start_date)
        events = [event for event in events if event["start_time"] >= start]

    if end_date:
        end = datetime.fromisoformat(end_date)
        events = [event for event in events if event["start_time"] <= end]

    return events

@app.get("/api/emails", response_model=List[EmailSummaryModel])
async def get_email_summaries(
    session: Dict = Depends(get_or_create_session)
):
    """
    Get email summaries for the current user.
    """
    return session["state"]["email_summaries"]

# Cleanup job to remove stale sessions (would run periodically in production)
def cleanup_sessions():
    """
    Remove inactive sessions older than 24 hours.
    """
    now = datetime.now()
    expired = []

    for user_id, session in user_sessions.items():
        if (now - session["last_activity"]).total_seconds() > 86400:  # 24 hours
            expired.append(user_id)

    for user_id in expired:
        del user_sessions[user_id]

if __name__ == "__main__":
    # Run the server
    uvicorn.run("api_server:app", host="0.0.0.0", port=8000, reload=True)