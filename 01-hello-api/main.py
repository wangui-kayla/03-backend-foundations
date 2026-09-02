from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "name": "RoboAPI",
        "description": "I don't have a cool name for my first API lol",
        "version": "1.0.0"
    }