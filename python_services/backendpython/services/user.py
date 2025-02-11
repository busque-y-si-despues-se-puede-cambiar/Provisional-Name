"""This module is used to handle data related to questions.

Author: Tito Alejandro Burbano Plazas <taburbanop@udistrital.edu.co>"""

from typing import List
from ..repositories.user import UserRepository, UserDAO


class UserServices:
    """This class has the services for user searches."""

    def __init__(self):
        self.repository = UserRepository()

    def get_all(self) -> List[UserDAO]:
        """This method is used to get all users.

        Returns:
            A list of users.
        """
        return self.repository.get_users()

    def get_by_username(self, username: str) -> List[UserDAO]:
        """This method is used to get users by username.

        Args:
            username (str): The username to be searched.

        Returns:
            A list of users with the matching username.
        """
        response = []
        for user in self.repository.get_users():
            if username.lower() in user.username.lower():
                response.append(user)
        return response
    
   
    def get_leaderboard(self, top_n: int = None) -> List[dict]:
     """This method returns the leaderboard sorted by score with only username and score."""
     users = self.repository.get_users_sorted_by_score()
     return users[:top_n] if top_n else users
