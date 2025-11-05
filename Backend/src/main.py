from fastapi import FastAPI

app = FastAPI(title="Hotel-IQ")

@app.get("/")
def check_health():
    return {"message": "Hello, The server is healthy"}

