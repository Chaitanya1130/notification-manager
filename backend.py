import os
import json
import openai
from dotenv import load_dotenv
from models import NotificationRequest, NotificationResponse

# Load environment variables
load_dotenv()

# Configure OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

class NotificationManager:
    def __init__(self):
        # Load context data if available
        self.context_data = self._load_context_data()
    
    def _load_context_data(self):
        """Load context data for enhanced notification generation"""
        try:
            if os.path.exists("dummy_data.json"):
                with open("dummy_data.json", "r") as f:
                    return json.load(f)
            return []
        except Exception as e:
            print(f"Error loading context data: {e}")
            return []
    
    def _get_recipient_history(self, recipient_id):
        """Get notification history for a specific recipient"""
        return [item for item in self.context_data if item["recipient_id"] == recipient_id]
    
    async def generate_notification(self, request: NotificationRequest) -> NotificationResponse:
        """Generate a smart notification using OpenAI"""
        
        # Get recipient history for context
        recipient_history = self._get_recipient_history(request.recipient_id)
        
        # Construct prompt for OpenAI
        system_prompt = """
        You are a smart notification system for an educational platform.
        Your job is to generate personalized, actionable notifications based on events and context.
        Make notifications concise, specific, and helpful with a clear next step.
        Always use the recipient's ID directly in the message instead of placeholders like [Recipient's Name].
        """
        
        user_prompt = f"""
        Recipient ID: {request.recipient_id}
        Event: {request.event}
        Action Required: {request.action_required}
        Additional Context: {request.prompt}
        
        Recipient History: {json.dumps(recipient_history) if recipient_history else "No previous history"}
        
        Generate a personalized notification message that is concise and actionable.
        Always address the recipient directly using their ID ({request.recipient_id}) instead of using placeholders.
        """
        
        try:
            # Call OpenAI API
            client = openai.OpenAI()
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=100,
                temperature=0.7
            )
            
            # Extract and clean the message
            message = response.choices[0].message.content.strip()
            
            # Return formatted response
            return NotificationResponse(message=message)
            
        except Exception as e:
            # Fallback message in case of API error
            print(f"Error generating notification: {e}")
            return NotificationResponse(
                message=f"Reminder: Action required for {request.event}. {request.action_required}."
            ) 