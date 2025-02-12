"""This module is used to handle data related to questions.

Author: Tito Alejandro Burbano Plazas <taburbanop@udistrital.edu.co>"""

import json
from typing import List
from pydantic import BaseModel
from backendpython.environment_variables import EnvironmentVariables


class UserDAO(BaseModel):
    """This class is used to define the data structure related to users."""
    username: str
    password: str
    score: int


class UserRepository:
    """This class represents the behavior of a repository to handle users data."""

    def __init__(self):
        """Initialize the class and load users data from file."""
        env = EnvironmentVariables()
        path_file = env.path_users_data
        self._load_data(path_file)

    def _load_data(self, path_file: str):
        try:
            with open(path_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            if "users" in data and isinstance(data["users"], list):
                self.data = data["users"]
            else:
                print("ERROR: Invalid JSON format, 'users' key missing or incorrect.")
                self.data = []

        except Exception as e:
            print(f"ERROR loading users: {e}")
            self.data = []

    def get_users(self) -> List[UserDAO]:
        """This method is used to get all users."""
        users = []
        for user in self.data:
            user_temp = UserDAO(
                id=user["id"],
                username=user["username"],
                password=user["password"],
                score=user["score"],
            )
            users.append(user_temp)
        return users

    def get_users_sorted_by_score(self) -> List[dict]:
     """This method returns users sorted by score in descending order, only showing username and score."""
     users = sorted(self.get_users(), key=lambda u: u.score, reverse=True)
     return [{"username": u.username, "score": u.score} for u in users]
