"""
This module defines API routes related to users in a game system.
FastAPI tools are used to expose endpoints.

Authors: 
Tito Alejandro Burbano Plazas <taburbanop@udistrital.edu.co>
Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>  
"""

from typing import List
from fastapi import APIRouter, HTTPException
from ..services.user import UserServices
from ..repositories.user import UserDAO

router = APIRouter()

services = UserServices()


@router.get("/users/all")
def get_all() -> List[UserDAO]:
    """
    Method used to get all users.
    
    This method does not receive input parameters. Returns a list of 'UserDAO' objects, 
    each representing a user with its related information.

    Returns:
        List[UserDAO]: List of 'UserDAO' objects that represent all users.
    """
    return services.get_all()


@router.get("/users/by_username/{username}")
def get_by_username(username: str) -> List[UserDAO]:
    """
    Method used to get users by their username.
    
    If the provided username is empty, an HTTP exception with code 400 is raised. 
    If the username is valid, a list of 'UserDAO' objects representing the users is returned 
    whose username matches the provided parameter.

    Args:
        username (str): The username to search for.

    Returns:
        List[UserDAO]: List of 'UserDAO' objects that represent users with the given username.
    
    Raises:
        HTTPException: If the username is an empty string, an HTTP 400 exception is thrown.
    """
    if username == "":
        raise HTTPException(status_code=400, detail="The username cannot be empty.")
    return services.get_by_username(username)

@router.get("/users/leaderboard")
def get_leaderboard(top_n: int = None) -> List[dict]:
    """
    Method that returns the ranking of users ordered by their score,
    showing only their username and score.
    
    If a 'top_n' parameter is passed, only the 'top_n' of users with the best 
    scores are returned. If the parameter is not passed, all users 
    are returned ordered by score.

    Args:
        top_n (int, optional): The number of users to show in the ranking. If None, shows all users.

    Returns:
        List[dict]: List of dictionaries with the username and its score.
    """
    return services.get_leaderboard(top_n)
