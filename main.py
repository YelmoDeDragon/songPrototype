from fastapi import FastAPI
from fastapi import Query
from pydantic import BaseModel
from typing import List
from spotify_agent import SpotifyAgent

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "pong"}


class Song(BaseModel):
    name: str
    artist: str

class Response(BaseModel):
    items: List[Song]

# http://localhost:8000/songs/suggestions?q=tu_busqueda
@app.get("/songs/suggestions")
async def suggestions(q: str = Query(..., min_length=4)):
    agent = SpotifyAgent()
    result = agent.search_songs(q)
    return result
