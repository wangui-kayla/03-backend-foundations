from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

games_db = [
    {
        "id": 1,
        "name": "Minecraft",
        "description": "A block based sandbox where players build 3D worlds and survive in it by being resourceful",
        "version": "26.3",
        "company": "Mojang Studios",
        "genre": "Sandbox"
    },

    {
        "id": 2,
        "name": "Genshin Impact",
        "description": "Open world action role-playing game that follows the journey of a sibling looking for another sibling",
        "version": "7.0",
        "company": "HoYoverse",
        "genre": "Action RPG"
    },

    {
        "id": 3,
        "name": "Fortnite",
        "description": "A vibrant battle royale sandbox that is basically last man standing with 100 players",
        "version": "31.00",
        "company": "Epic Games",
        "genre": "Battle Royale"
    },

    {
        "id": 4,
        "name": "Roblox",
        "description": "Online platform that allows users to create their own games and play many experiences created by the users",
        "version": "2.640",
        "company": "Roblox Corporation",
        "genre": "Massively Multiplayer Online"
    },

    {
        "id": 5,
        "name": "Call Of Duty",
        "description": "A fast paced first person military shooter that has multiplayer mode and ranked systems",
        "version": "1.0.45",
        "company": "Activision",
        "genre": "First-Person Shooter"
    }
]

class Game(BaseModel):
    name: str
    description: str
    version: str
    company: str
    genre: str

class GameResponse(BaseModel):
    id: int
    name: str
    description: str
    version: str
    company: str
    genre: str

class GameUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    version: str | None = None
    company: str | None = None
    genre: str | None = None

@app.get("/games", response_model=list[GameResponse])
def get_games(company: str | None = None):

    if company is None:
        return games_db

    matching_games = []

    for game in games_db:
        if game["company"] == company:
            matching_games.append(game)

    if not matching_games:
        return matching_games

@app.get("/games/{game_id}", response_model=GameResponse)
def get_game(game_id: int):
    for game in games_db:
        if game["id"] == game_id:
            return game
    raise HTTPException(status_code=404, detail="Game not found")

@app.post("/games", status_code=201, response_model=GameResponse)
def create_game(game: Game):

    new_id = len(games_db) + 1

    new_game = {
        "id": new_id,
        "name": game.name,
        "description": game.description,
        "version": game.version,
        "company": game.company,
        "genre": game.genre,
        "secret": "this should not be returned"
    }

    games_db.append(new_game)

    return new_game

@app.put("/games/{game_id}")
def update_game(game_id: int, game: Game):
    for existing_game in games_db:
        if existing_game["id"] == game_id:
            existing_game["name"] = game.name
            existing_game["description"] = game.description
            existing_game["version"] = game.version
            existing_game["company"] = game.company
            existing_game["genre"] = game.genre

            return existing_game

    raise HTTPException(status_code=404, detail="Game not found")

@app.patch("/games/{game_id}")
def update_game_section(game_id: int, game:GameUpdate):
    for existing_game in games_db:
        if existing_game["id"] == game_id:
            if game.name is not None:
                existing_game["name"] = game.name
            if game.description is not None:
                existing_game["description"] = game.description
            if game.version is not None:
                existing_game["version"] = game.version
            if game.company is not None:
                existing_game["company"] = game.company
            if game.genre is not None:
                existing_game["genre"] = game.genre

            return existing_game

    raise HTTPException(status_code=404, detail="Game not found")

@app.delete("/games/{game_id}")
def delete_game(game_id: int):
    for existing_game in games_db:
        if existing_game["id"] == game_id:
            games_db.remove(existing_game)
            return existing_game

    raise HTTPException(status_code=404, detail=f"Game with ID {game_id} not found")