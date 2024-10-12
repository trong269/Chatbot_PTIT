from passlib.context import CryptContext
from fastapi import HTTPException
import re
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify_password(raw_password, hased_password):
    return pwd_context.verify(raw_password, hased_password)

def validate_password_strength(password: str):
    # Yêu cầu mật khẩu mạnh: ít nhất 8 ký tự, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt
    if len(password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters long")
    if not re.search(r"[A-Z]", password):
        raise HTTPException(status_code=400, detail="Password must contain at least one uppercase letter")
    if not re.search(r"[a-z]", password):
        raise HTTPException(status_code=400, detail="Password must contain at least one lowercase letter")
    if not re.search(r"\d", password):
        raise HTTPException(status_code=400, detail="Password must contain at least one number")
    if not re.search(r"[!@#\$%\^&\*]", password):
        raise HTTPException(status_code=400, detail="Password must contain at least one special character")
    return True