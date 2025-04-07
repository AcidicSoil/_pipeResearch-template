# AI Secretary - Mobile AI Assistant

A powerful mobile AI assistant designed for knowledge workers. It provides task management, calendar event processing, email summarization, and natural conversations with on-device processing for privacy-sensitive operations and cloud capabilities for complex computations.

## Features

- **Natural Language Understanding**: Process and understand user queries with sophisticated intent classification
- **Task Management**: Create, track, and prioritize tasks through natural language
- **Calendar Integration**: Schedule and manage calendar events conversationally
- **Email Summarization**: Extract key information and action items from emails
- **Voice Interface**: Process speech using on-device Whisper.cpp for privacy and efficiency
- **Hybrid Processing**: Intelligently route requests between on-device and cloud processing
- **Privacy-First**: Prioritize on-device processing for sensitive data
- **Emotion Recognition**: Basic sentiment analysis to enhance conversation quality

## Architecture

The application follows a layered architecture:

1. **Frontend Layer** (Mobile App): Flutter-based cross-platform UI (planned)
2. **API Layer** (FastAPI): REST API endpoints for the mobile application
3. **Orchestration Layer** (LangGraph): Stateful workflow management for complex interactions
4. **Hybrid Processing Layer**: Intelligent routing between on-device and cloud processing
5. **Local Inference Layer**: On-device models for privacy-sensitive operations

## Getting Started

### Prerequisites

- Python 3.8+ with pip
- OpenAI API key (for cloud processing)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-secretary.git
cd ai-secretary
```

2. Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys and configuration
```

### Running the API Server

Start the FastAPI server:
```bash
python api_server.py
```

The API will be available at http://localhost:8000.

### Testing

Run the test suite:
```bash
pytest
```

Or run specific tests:
```bash
python test_secretary.py
```

## Components

### 1. LangGraph Orchestration

The core of the application uses LangGraph for stateful workflows:

```python
from secretary_graph import create_workflow, initialize_state
from langchain.schema import HumanMessage

# Create the workflow
workflow = create_workflow()

# Initialize state
state = initialize_state()

# Process a user message
state["messages"] = [HumanMessage(content="Schedule a meeting tomorrow at 2pm")]
result = workflow.invoke(state)
```

### 2. Hybrid Processing

For intelligent routing between on-device and cloud processing:

```python
from hybrid_processing import HybridProcessor, ProcessingRequest, Capability

processor = HybridProcessor()

request = ProcessingRequest(
    user_id="user123",
    input_text="What's on my calendar today?",
    required_capabilities=[Capability.BASIC_NLP, Capability.CALENDAR_INTEGRATION],
    privacy_level=5
)

result = processor.process(request)
print(f"Processed on: {result.processing_location}")
```

### 3. Voice Processing

For on-device speech recognition:

```python
from voice_processor import VoiceProcessor

processor = VoiceProcessor()

with open("audio_file.wav", "rb") as f:
    audio_data = f.read()

result = processor.process_voice(audio_data)
print(f"Transcription: {result['transcription']['text']}")
print(f"Emotion: {result['emotion']['primary_emotion']}")
```

## API Endpoints

The FastAPI server provides these main endpoints:

- **POST /api/conversation**: Process a user message and return AI response
- **GET /api/tasks**: Get all tasks for the current user
- **POST /api/tasks**: Create a new task
- **PUT /api/tasks/{task_id}**: Update an existing task
- **GET /api/calendar**: Get calendar events
- **GET /api/emails**: Get email summaries

## License

MIT

## Acknowledgments

- Built with [LangGraph](https://github.com/langchain-ai/langgraph)
- Uses [Whisper.cpp](https://github.com/ggerganov/whisper.cpp) for on-device speech recognition
- Powered by OpenAI's language models