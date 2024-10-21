from typing import List
from fastapi import status, HTTPException, Depends, APIRouter, FastAPI, Response
from sqlalchemy.orm import Session
from .. import schemas, utils, models, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/chat",
    tags=['chat']
)

