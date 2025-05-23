import json
import random

def generate_dummy_data(num_entries=10):
    """Generate dummy notification data for testing"""
    
    recipient_types = ["T", "S"]  # T for teachers, S for students
    
    events = [
        "Low Quiz Completion",
        "Assignment Overdue",
        "Engagement Drop",
        "Performance Decline",
        "Course Completion Risk",
        "Missing Lecture",
        "Discussion Participation Low",
        "Grade Update"
    ]
    
    actions = [
        "Send nudge",
        "Request meeting",
        "Send reminder",
        "Suggest intervention",
        "Request feedback"
    ]
    
    prompts = [
        "Send smart reminders based on overdue tasks or engagement dips.",
        "Notify teacher about student at risk of falling behind.",
        "Remind students about upcoming deadlines.",
        "Alert teacher to low class participation.",
        "Suggest personalized intervention for struggling student."
    ]
    
    data = []
    
    for i in range(num_entries):
        recipient_type = random.choice(recipient_types)
        recipient_id = f"{recipient_type}{random.randint(1, 999):03d}"
        
        entry = {
            "recipient_id": recipient_id,
            "event": random.choice(events),
            "action_required": random.choice(actions),
            "prompt": random.choice(prompts)
        }
        
        data.append(entry)
    
    return data

def save_dummy_data(filename="dummy_data.json", num_entries=10):
    """Save dummy data to a JSON file"""
    data = generate_dummy_data(num_entries)
    
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    
    return filename

if __name__ == "__main__":
    save_dummy_data(num_entries=20)
    print("Dummy data generated and saved to dummy_data.json") 