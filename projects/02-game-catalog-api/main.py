from fastapi import FastAPI, HTTPException

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

@app.get("/games")
def get_games():
    return games_db

@app.get("/games/{game_id}")
def get_game(game_id: int):
    for game in games_db:
        if game["id"] == game_id:
            return game
        else:
            raise HTTPException(
                status_code=404,
                detail="Game not found"
            )

'''
@app.get("/games")
def get_games(genre: str | None = None):
'''
