from database import SessionLocal
from models import ConversationModel

db = SessionLocal()

conversations = db.query(ConversationModel).all()

for c in conversations:
    print(c.user_id, c.content)