from sqlalchemy.orm import Session
from models import ConversationModel, PreferencesModel, MilestoneModel


def add_conversation(db: Session, conversation):
    db_obj = ConversationModel(
        user_id=conversation.user_id,
        turn_id=conversation.turn_id,
        role=conversation.role,
        content=conversation.content,
        timestamp=conversation.timestamp
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj


def get_user_conversations(db: Session, user_id: str):
    return db.query(ConversationModel).filter(
        ConversationModel.user_id == user_id
    ).all()


def add_milestone(db: Session, milestone):

    db_obj = MilestoneModel(
        milestone_id=milestone.milestone_id,
        user_id=milestone.user_id,
        description=milestone.description,
        status=milestone.status,
        date_achieved=milestone.date_achieved
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj