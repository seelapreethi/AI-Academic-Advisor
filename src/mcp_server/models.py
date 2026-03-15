from sqlalchemy import Column, String, Integer, DateTime, Text
from datetime import datetime
from database import Base


class ConversationModel(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    turn_id = Column(Integer)
    role = Column(String)
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)


class PreferencesModel(Base):
    __tablename__ = "preferences"

    user_id = Column(String, primary_key=True)
    preferences = Column(Text)


class MilestoneModel(Base):
    __tablename__ = "milestones"

    milestone_id = Column(String, primary_key=True)
    user_id = Column(String, index=True)
    description = Column(Text)
    status = Column(String)
    date_achieved = Column(DateTime)