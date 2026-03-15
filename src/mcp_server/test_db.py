from database import SessionLocal
from memory_schemas import Conversation
from crud import add_conversation

db = SessionLocal()

conv = Conversation(
    user_id="student1",
    turn_id=1,
    role="user",
    content="I want to learn AI"
)

add_conversation(db, conv)

print("Conversation stored successfully")