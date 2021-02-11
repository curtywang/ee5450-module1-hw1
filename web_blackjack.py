import uvicorn
from typing import Optional
from fastapi import FastAPI, HTTPException, Path, status, Query
from blackjack_db import AsyncBlackjackGameDB, Blackjack


BLACKJACK_DB = AsyncBlackjackGameDB()
app = FastAPI(
    title="Blackjack Server",
    description="Implementation of a simultaneous multi-game Blackjack server by[Your name here]."
)


async def get_game(game_id: str) -> Blackjack:
    """
    Get a game from the blackjack game database, otherwise raise a 404.

    :param game_id: the uuid in str of the game to retrieve
    """
    the_game = await BLACKJACK_DB.get_game(game_id)
    if the_game is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Game {game_id} not found.")
    return the_game


@app.get('/')
async def home():
    return {"message": "Welcome to Blackjack!"}


""" TODO: Add your code here. """


if __name__ == '__main__':
    # running from main instead of terminal allows for debugger
    uvicorn.run('web_blackjack:app', port=8000, log_level='info', reload=True)
