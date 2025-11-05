from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from constants import ALLOWED_ORIGINS

app = FastAPI(title="Hotel-IQ")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def check_health():
    return {"message": "Hello, The server is healthy"}

