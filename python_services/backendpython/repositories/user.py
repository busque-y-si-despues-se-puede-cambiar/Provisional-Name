"""
This module defines the classes and methods related to the management of user data, 
including the user data structure and the management of its storage in a JSON file.

Authors: 
Tito Alejandro Burbano Plazas <taburbanop@udistrital.edu.co>
Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>
"""

import json
from typing import List
from pydantic import BaseModel
from backendpython.environment_variables import EnvironmentVariables


class UserDAO(BaseModel):
    """
    This class defines the data structure related to users.
    """
    id: int
    username: str
    password: str
    score: int
    online: bool
    admin: bool


class UserRepository:
    """
    This class manages the retrieval and storage of user data.
    """

    def __init__(self):
        """
        Initialize the class and load users data from file.
        """
        env = EnvironmentVariables()
        self.path_file = env.path_users_data
        self._load_data()

    def _load_data(self):
        """
        Load users from JSON file.
        """
        try:
            with open(self.path_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.data = [UserDAO(**user) for user in data.get("users", [])]
        except Exception as e:
            print(f"ERROR loading users: {e}")
            self.data = []

    def get_users(self) -> List[UserDAO]:
        """
        Retrieve all users.
        """
        return self.data

    def save_users(self, users: List[UserDAO]):
        """
        Save updated user list back to the JSON file.
        """
        try:
            with open(self.path_file, "w", encoding="utf-8") as f:
                json.dump({"users": [user.model_dump() for user in users]}, f, indent=4)
        except Exception as e:
            print(f"ERROR saving users: {e}")

    def get_users_sorted_by_score(self) -> List[dict]:
        """
        This method returns users sorted by score in descending order,
        only showing username and score.
        """
        users = sorted(self.get_users(), key=lambda u: u.score, reverse=True)
        return [{"username": u.username, "score": u.score} for u in users]
