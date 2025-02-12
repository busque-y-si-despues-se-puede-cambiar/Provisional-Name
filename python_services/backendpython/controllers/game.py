"""
This module defines API routes related to the game system.
FastAPI tools are used to expose endpoints.

Authors: 
Tito Alejandro Burbano Plazas <taburbanop@udistrital.edu.co>
Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>  
"""

from fastapi import APIRouter, HTTPException
from ..services.game_session import GameSession

router = APIRouter()
@router.post("/game/start/{username}")
def start_game(username: str):
    """
    This method starts a game session for a registered user.

    The function creates a new instance of 'GameSession' for the given user, 
    starts the game and returns a message indicating whether the session is complete, 
    along with the final score obtained by the user.

    Args:
        username (str): The username for which the game session is started.

    Returns:
        dict: A dictionary containing a message indicating that the session has completed 
              and the final score obtained by the user.
    
    Raises:
        HTTPException: If an error occurs during game execution, an HTTP 400 exception is 
                       thrown with the details of the error.
    """
    try:
        game = GameSession(username)
        game.play()
        return {"message": "Game session finished", "final_score": game.score}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))