from fastapi import APIRouter
from database import SessionLocal
from memory_schemas import Conversation
from crud import add_conversation
from models import ConversationModel
from vector_store import store_embedding, search_similar

router = APIRouter()


# WRITE MEMORY
@router.post("/memory/write")
def memory_write(conversation: Conversation):

    db = SessionLocal()

    try:
        # store in sqlite
        add_conversation(db, conversation)

        # store embedding in vector db
        store_embedding(conversation.content, conversation.turn_id)

        return {
            "status": "stored",
            "turn_id": conversation.turn_id
        }

    finally:
        db.close()


# READ MEMORY
@router.get("/memory/read")
def memory_read(user_id: str, limit: int = 5):

    db = SessionLocal()

    try:
        conversations = (
            db.query(ConversationModel)
            .filter(ConversationModel.user_id == user_id)
            .order_by(ConversationModel.timestamp.desc())
            .limit(limit)
            .all()
        )

        return [
            {
                "user_id": c.user_id,
                "turn_id": c.turn_id,
                "role": c.role,
                "content": c.content,
                "timestamp": c.timestamp
            }
            for c in conversations
        ]

    finally:
        db.close()


# VECTOR MEMORY SEARCH
@router.get("/memory/context_search")
def memory_retrieve_by_context(query: str):

    results = search_similar(query)

    return {
        "query": query,
        "results": results
    }