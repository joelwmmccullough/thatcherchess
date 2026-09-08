"""FastAPI server for ThatcherChess"""

"""Checks if app is available and retursn true"""

from fastapi import FastAPI
app = FastAPI(title="ThatcherChess")

@app.get("/api/ping")
def ping() -> dict:
    return {"okiedokie": True}