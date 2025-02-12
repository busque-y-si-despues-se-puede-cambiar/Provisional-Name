"""
This module contains the `UserServices` class, which provides 
several methods to interact with user data.

Take advantage of the `UserRepository` class to retrieve and manage users.

Authors:
Tito Alejandro Burbano Plazas <taburbanop@udistrital.edu.co>
Author: Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>
"""

from typing import List
from ..repositories.user import UserRepository, UserDAO


class UserServices:
    """
    This class provides services for managing and retrieving user information.
    """


    def __init__(self):
        """
        Initializes the UserServices class and sets up the UserRepository.
        The repository is used to interact with the underlying data source for user information.
        """
        self.repository = UserRepository()

    def get_all(self) -> List[UserDAO]:
        """
        Fetches all users from the repository.

        This method interacts with the UserRepository to retrieve a complete list of all users.

        Returns:
            List[UserDAO]: A list of UserDAO objects representing all users in the system.
        """
        return self.repository.get_users()

    def get_by_username(self, username: str) -> List[UserDAO]:
        """
        Fetches users based on a partial or full username match.

        This method searches for users whose username contains the given search string,
        case-insensitive.

        Args:
            username (str): The username or partial username to search for.

        Returns:
            List[UserDAO]: A list of UserDAO objects for users that match the search criteria.
        """
        response = []
        for user in self.repository.get_users():
            if username.lower() in user.username.lower():
                response.append(user)
        return response

    def get_leaderboard(self, top_n: int = None) -> List[dict]:
        """
        Fetches the leaderboard sorted by score.

        This method retrieves a list of users sorted by their score in descending order, 
        and optionally limits the result to the top `n` users.

        Args:
            top_n (int, optional): The number of top users to return. If not specified,
            all users are returned.

        Returns:
            List[dict]: A list of dictionaries, each containing the username 
            and score of the top users.
        """
        users = self.repository.get_users_sorted_by_score()
        return users[:top_n] if top_n else users
