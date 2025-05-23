from pydantic import BaseModel

class NotificationRequest(BaseModel):
    recipient_id: str
    event: str
    action_required: str
    prompt: str

class NotificationResponse(BaseModel):
    message: str 