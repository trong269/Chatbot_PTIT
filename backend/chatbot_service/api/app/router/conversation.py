from datetime import datetime
from typing import List
from fastapi import status, HTTPException, Depends, APIRouter, FastAPI, Response
from sqlalchemy.orm import Session
from .. import schemas, utils, models, oauth2
from ..database import get_db
from domain.chatbot import ChatBot

router = APIRouter(
    prefix="/conversations",
    tags=['conversations']
)


bot = ChatBot()
# history_messages = []

@router.get("/", response_model=List[schemas.ConversationResponse])
def get_conversation(db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    conversation_query = db.query(models.Conversation).filter(models.Conversation.user_id == current_user.user_id).order_by(models.Conversation.conversation_id.asc())
    if not conversation_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User: {current_user.user_id} doesn't have conversations")
    
    return conversation_query.all()
    # return "ok"

# Khởi tạo cuộc trò chuyện mới khi người dùng bắt đầu phiên trò chuyện
@router.post("/", response_model=schemas.ConversationResponse)
def start_conversation(title: str, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    if title == None or title.strip() == "":
        raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED, detail=f"You must enter a valid title")
    conversation = models.Conversation(user_id=current_user.user_id, title = title, end_time = None)
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    return conversation

@router.put("/{conversation_id}/end", response_model=schemas.ConversationResponse)
def end_conversation(conversation_id: int, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    # history_messages.clear()
    # Tìm kiếm conversation theo conversation_id
    conversation = db.query(models.Conversation).filter(models.Conversation.conversation_id == conversation_id,
                                                        models.Conversation.user_id == current_user.user_id
                                                        ).first()
    
    # Nếu không tìm thấy conversation
    if not conversation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")
    
    # Nếu conversation đã kết thúc
    if conversation.end_time is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Conversation already ended")
    
    # Cập nhật end_time với thời gian hiện tại
    conversation.end_time = datetime.now()
    db.commit()
    db.refresh(conversation)
    
    return conversation

@router.post("/{conversation_id}/messages", response_model=schemas.MessageResponse)
def add_message(conversation_id: int, message: schemas.MessageCreate, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    conversation = db.query(models.Conversation).filter(models.Conversation.conversation_id == conversation_id,
                                                        models.Conversation.end_time == None).first()
    if not conversation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Conversation {conversation_id} not found or already ended")
    
    new_message_user = models.Message(conversation_id=conversation_id, content=message.content, sender="user")
    db.add(new_message_user)
    db.commit()
    db.refresh(new_message_user)

    # Lấy lịch sử tin nhắn của cuộc trò chuyện hiện tại từ database
    history_messages = db.query(models.Message).filter(models.Message.conversation_id == conversation_id).order_by(models.Message.message_id.asc()).all()
    
    # Tạo lịch sử tin nhắn dạng chuỗi
    history = []
    for i, msg in enumerate(history_messages, 1):
        history_entry = f"câu hỏi số {i}: {msg.content}" if msg.sender == 'user' else f"câu trả lời: {msg.content}"
        history.append(history_entry)
    
    # Kết hợp lịch sử thành một chuỗi để truyền vào chatbot
    history_text = "\n".join(history)
    
    # Truyền lịch sử tin nhắn cho bot
    response_message = bot.chat(message.content, history_text)
 
    # response_message = bot.chat(message.content , "\n".join(history_messages))
    # history_number = str(len(history_messages)+1)
    # history = f"""câu hỏi số {history_number}: {message.content}
    # câu trả lời: {response_message}"""
    # history_messages.append(history)
    
    new_message_bot = models.Message(conversation_id=conversation_id, content=response_message, sender="bot")
    db.add(new_message_bot)
    db.commit()
    db.refresh(new_message_bot)

    return new_message_bot

@router.delete("/{conversation_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_conversation(conversation_id: int, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    conversation_query = db.query(models.Conversation).filter(models.Conversation.conversation_id == conversation_id,
                                  models.Conversation.user_id == current_user.user_id)
    
    if not conversation_query.first():
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Conversation {conversation_id} doesn't belong to you")
    
    conversation_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)