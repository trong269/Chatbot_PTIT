from typing import List
from fastapi import status, HTTPException, Depends, APIRouter, FastAPI, Response
from sqlalchemy.orm import Session
from .. import schemas, utils, models, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/conversations",
    tags=['conversations']
)

# Khởi tạo cuộc trò chuyện mới khi người dùng bắt đầu phiên trò chuyện
@router.post("/", response_model=schemas.ConversationResponse)
def start_conversation(title: str, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    conversation = models.Conversation(user_id=current_user, title = title)
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    return conversation

@router.get("/{id}", response_model=schemas.ConversationResponse)
def start_conversation(id: int, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    conversation_query = db.query(models.Conversation).filter(models.Conversation.user_id == current_user.user_id)
    if not conversation_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User: {current_user.user_id} doesn't have conversations")
    
    return conversation_query.first()

# Thêm tin nhắn vào cuộc trò chuyện
@router.post("/{conversation_id}/messages/", response_model=schemas.MessageResponse)
def add_message(conversation_id: int, message: schemas.MessageCreate, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    conversation = db.query(models.Conversation).filter(models.Conversation.conversation_id == conversation_id).first()
    if not conversation:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Conversation {conversation_id} not found")
    
    new_message = models.Message(conversation_id=conversation_id, content=message.content, sender="user")
    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    response_message = "Đây là phản hồi từ AI"
    
    new_message = models.Message(conversation_id=conversation_id, content=response_message, sender="bot")
    db.add(response_message)
    db.commit
    db.refresh(new_message)

    return new_message