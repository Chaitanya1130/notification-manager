# Notification Manager Agent

A smart notification system that sends automated reminders to teachers or students based on various triggers such as overdue tasks, engagement dips, or performance issues.

## Features

- FastAPI backend with RESTful API
- Smart notification generation using OpenAI
- Dummy data generator for testing
- Contextual awareness based on recipient history

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

## Usage

1. Start the server:
   ```
   python main.py
   ```
   This will automatically generate dummy data if none exists.

2. Generate dummy data (optional):
   ```
   curl "http://localhost:8000/generate-dummy-data?num_entries=20"
   ```

3. Send a notification request:
   ```
   curl -X POST "http://localhost:8000/notifications" \
     -H "Content-Type: application/json" \
     -d '{
       "recipient_id": "T001",
       "event": "Low Quiz Completion",
       "action_required": "Send nudge",
       "prompt": "Send smart reminders based on overdue tasks or engagement dips."
     }'
   ```

## API Documentation

Once the server is running, view the interactive API documentation at:
```
http://localhost:8000/docs
```

## Input Schema
```json
{
  "recipient_id": "T001",
  "event": "Low Quiz Completion",
  "action_required": "Send nudge",
  "prompt": "Send smart reminders based on overdue tasks or engagement dips."
}
```

## Output Schema
```json
{
  "message": "Reminder: Only 40% students completed this week's quiz. Suggest re-prompt."
}
``` 