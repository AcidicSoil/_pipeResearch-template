# Frontend Documentation

## Framework
**Flutter**

Chosen for:
- High performance on both Android and iOS
- Rich UI toolkit and animations
- Strong community and plugin ecosystem

## UI Architecture

### Main Screens
1. **Home Dashboard**
   - Shows prioritized task list
   - Daily agenda
   - Smart notifications (reminders, summaries)

2. **Smart Inbox**
   - Email summaries and categorized messages
   - Actionable insights (e.g., "Schedule meeting")

3. **Calendar View**
   - Day, week, month views
   - Natural language event creation

4. **Voice Interaction**
   - Push-to-talk UI
   - Transcription using Whisper.cpp (offline)
   - Command suggestions and feedback display

5. **Settings & Personalization**
   - Privacy preferences
   - Sync toggle (cloud/on-device)
   - Model behavior customization

### Navigation
- **Bottom Tab Bar**
  - Tabs: Home | Inbox | Calendar | Voice | Settings
  - Consistent across all screens

## Styling System
**Material 3 (Material You)**
- Responsive layout support
- Theming with system color adaptation
- Accessible and clean design

## Chat Interface
- Based on [`flutter_chat_ui`](https://pub.dev/packages/flutter_chat_ui)
- Custom avatars, message bubbles, and layout
- Dynamic response cards for LLM-generated replies
- Inline voice-to-text input

## Forms & Input Components
- Task input: Date, time, priority, natural language support
- Event creation: NLP support + manual fields
- Settings: Switches, dropdowns, and sliders

## Accessibility
- Voice control integration
- High-contrast mode
- Font resizing
- Screen reader support with semantic labels

## Offline Support UI
- Status banner for offline mode
- Graceful fallback for disabled features
- Local caching for events, tasks, and messages