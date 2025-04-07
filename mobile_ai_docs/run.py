#!/usr/bin/env python3
"""
AI Secretary Startup Script
--------------------------
This script provides a convenient way to start the AI Secretary components.
"""

import os
import sys
import argparse
import subprocess
import logging
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("ai_secretary")

# Load environment variables
load_dotenv()

def start_api_server(port=None, host=None):
    """Start the FastAPI server."""
    api_port = port or os.getenv("API_PORT", "8000")
    api_host = host or os.getenv("API_HOST", "0.0.0.0")

    logger.info(f"Starting API server on {api_host}:{api_port}")

    try:
        subprocess.run([
            sys.executable, "api_server.py",
            "--host", api_host,
            "--port", api_port
        ], check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to start API server: {e}")
        sys.exit(1)

def run_test(test_file=None):
    """Run tests."""
    if test_file:
        logger.info(f"Running test file: {test_file}")
        try:
            subprocess.run([sys.executable, test_file], check=True)
        except subprocess.CalledProcessError as e:
            logger.error(f"Tests failed: {e}")
            sys.exit(1)
    else:
        logger.info("Running all tests with pytest")
        try:
            subprocess.run(["pytest", "-v"], check=True)
        except subprocess.CalledProcessError as e:
            logger.error(f"Tests failed: {e}")
            sys.exit(1)

def demo_conversation():
    """Run a demonstration conversation with the AI Secretary."""
    logger.info("Starting AI Secretary conversation demo")

    try:
        from secretary_graph import create_workflow, initialize_state
        from langchain.schema import HumanMessage, AIMessage
        import json

        # Create the workflow
        workflow = create_workflow()

        # Initialize state
        state = initialize_state()

        # Sample conversation
        demo_inputs = [
            "Hello, I'm new here. What can you help me with?",
            "I need to schedule a meeting with the team tomorrow at 3pm.",
            "Remind me to prepare the presentation slides by 5pm today.",
            "Did I get any important emails from Sarah about the project?",
            "What's my schedule for tomorrow?"
        ]

        # Configuration for user session
        config = {"configurable": {"thread_id": "demo_user"}}

        print("\n" + "=" * 50)
        print("AI Secretary Conversation Demo")
        print("=" * 50)

        for i, user_input in enumerate(demo_inputs):
            print(f"\nUser: {user_input}")

            # Add user message
            state["messages"].append(HumanMessage(content=user_input))

            # Process with workflow
            result = workflow.invoke(state, config=config)

            # Update state for next iteration
            state = result

            # Get AI response
            ai_messages = [msg for msg in state["messages"] if isinstance(msg, AIMessage)]
            if ai_messages:
                latest_ai_message = ai_messages[-1]
                print(f"AI Secretary: {latest_ai_message.content}")

        print("\n" + "=" * 50)
        print("Demo completed! Here's the final state:")
        print("Tasks:", len(state["tasks"]))
        print("Calendar events:", len(state["calendar_events"]))
        print("Email summaries:", len(state["email_summaries"]))
        print("=" * 50)

    except Exception as e:
        logger.error(f"Demo failed: {e}")
        sys.exit(1)

def download_models():
    """Download required models for on-device processing."""
    logger.info("Downloading required models")

    try:
        # Create models directory
        os.makedirs("models", exist_ok=True)

        # Download Whisper model
        from voice_processor import VoiceProcessor
        whisper_model_path = VoiceProcessor.download_model("small.en")
        logger.info(f"Whisper model available at: {whisper_model_path}")

        # In a real implementation, we would download additional models here
        logger.info("Model download completed")

    except Exception as e:
        logger.error(f"Failed to download models: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Secretary Startup Script")

    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # API server command
    api_parser = subparsers.add_parser("api", help="Start the API server")
    api_parser.add_argument("--port", type=str, help="Port to run the API server on")
    api_parser.add_argument("--host", type=str, help="Host to run the API server on")

    # Test command
    test_parser = subparsers.add_parser("test", help="Run tests")
    test_parser.add_argument("--file", type=str, help="Specific test file to run")

    # Demo command
    demo_parser = subparsers.add_parser("demo", help="Run a conversation demo")

    # Download models command
    download_parser = subparsers.add_parser("download", help="Download required models")

    # Parse arguments
    args = parser.parse_args()

    # Execute command
    if args.command == "api":
        start_api_server(args.port, args.host)
    elif args.command == "test":
        run_test(args.file)
    elif args.command == "demo":
        demo_conversation()
    elif args.command == "download":
        download_models()
    else:
        # Default to showing help
        parser.print_help()