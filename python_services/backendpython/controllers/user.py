"""This module is used to handle data related to questions.

Author: Tito Alejandro Burbano Plazas <taburbanop@udistrital.edu.co>"""

from typing import List
from fastapi import APIRouter, HTTPException
from ..services.user import UserServices
from ..repositories.user import UserDAO

router = APIRouter()

services = UserServices()


@router.get("/users/all")
def get_all() -> List[UserDAO]:
    """This method is used to get all users."""
    return services.get_all()


@router.get("/users/by_username/{username}")
def get_by_username(username: str) -> List[UserDAO]:
    """This method is used to get users by username."""
    if username == "":
        raise HTTPException(status_code=400, detail="The username cannot be empty.")
    return services.get_by_username(username)

@router.get("/users/leaderboard")
def get_leaderboard(top_n: int = None) -> List[dict]:
    """This method returns the leaderboard sorted by score with only username and score."""
    return services.get_leaderboard(top_n)