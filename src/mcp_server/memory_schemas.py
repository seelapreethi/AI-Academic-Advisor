from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Dict, Any, Optional


class Conversation(BaseModel):
    user_id: str
    turn_id: int
    role: str  # 'user' or 'assistant'
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class UserPreferences(BaseModel):
    user_id: str
    preferences: Dict[str, Any]


class Milestone(BaseModel):
    user_id: str
    milestone_id: str
    description: str
    status: str  # 'completed', 'in-progress', 'planned'
    date_achieved: Optional[datetime] = None