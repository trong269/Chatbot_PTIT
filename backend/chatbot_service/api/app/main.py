from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .router import auth, user, conversation
# models.Base.metadata.create_all(bind = engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # hoặc ["*"] để cho phép tất cả
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(conversation.router)

@app.get("/")
def check():
    return{"message": "Hello"}
 