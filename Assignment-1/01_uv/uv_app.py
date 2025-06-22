# 01_uv/uv_app.py

from fastapi import FastAPI

app = FastAPI()

# Home Route
@app.get("/")
def home():
    return {
        "developer": "Kanwal Rafiqe",
        "course": "Quarter 4 - Agentic AI",
        "message": "Hello from Kanwal Rafiqe + FastAPI! 🚀"
    }

# About Route
@app.get("/about")
def about():
    return {
        "info": "This is a basic FastAPI app created for my first Agentic AI assignment.",
        "learning": "FastAPI, Uvicorn, Python"
    }
