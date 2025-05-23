import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from models import NotificationRequest, NotificationResponse
from backend import NotificationManager
from data_generator import save_dummy_data

# Initialize the app
app = FastAPI(
    title="Notification Manager API",
    description="Send smart, automated reminders based on triggers",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize notification manager
notification_manager = NotificationManager()

@app.post("/notifications", response_model=NotificationResponse)
async def create_notification(request: NotificationRequest):
    """
    Generate a smart notification based on the provided event and context.
    """
    try:
        response = await notification_manager.generate_notification(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # Run the application
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 