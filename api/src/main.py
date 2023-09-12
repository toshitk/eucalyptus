from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.presentation.controller import users_router

app = FastAPI()
allow_origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users_router)
