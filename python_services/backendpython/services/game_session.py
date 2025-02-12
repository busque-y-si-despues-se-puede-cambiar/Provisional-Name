"""
This module contains the `GameSession` class, which is responsible 
for managing the game sessions for online users.

Authors:
Tito Alejandro Burbano Plazas <taburbanop@udistrital.edu.co>
Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>
"""
import random
from ..repositories.user import UserRepository
from ..repositories.question import QuestionRepository

class GameSession:
    """
    This class manages the game session for an online user. It handles the core logic of the game.
    """

    def __init__(self, username: str):
        """
        Initializes the GameSession class with the given username. 
        It fetches the user from the repository and sets up the 
        game environment by initializing score and lives.

        Args:
            username (str): The username of the user who is starting the game.
        
        Raises:
            ValueError: If the user is not found or not online.
        """
        self.user_repo = UserRepository()
        self.question_repo = QuestionRepository()
        self.user = self._get_online_user(username)
        self.score = 0
        self.lives = 3

    def _get_online_user(self, username: str):
        """
        This private method retrieves the user from the repository if they are online.
        Raises an error if the user is not online or does not exist.

        Args:
            username (str): The username of the user to be retrieved.

        Returns:
            UserDAO: The user object if the user is online.

        Raises:
            ValueError: If the user is not found or not online.
        """
        users = self.user_repo.get_users()
        for user in users:
            if user.username == username and user.online:
                return user
        raise ValueError("User is not online or does not exist.")

    def play(self):
        """
        Starts the game session for the user. The user is presented with random questions and 
        can answer by selecting one of the options. The user earns points for correct answers 
        and loses lives for incorrect answers. The game continues until the user runs out of lives.

        The final score is displayed at the end, and the user's score is updated in the repository.
        """
        print(f"Welcome {self.user.username}, let's play! You have {self.lives} lives.")

        while self.lives > 0:
            question = random.choice(self.question_repo.get_questions())
            print(f"\n{question.statement}")
            print(f"1. {question.correctAnswer}")
            print(f"2. {question.answer2}")
            print(f"3. {question.answer3}")
            print(f"4. {question.answer4}")

            try:
                answer = int(input("Choose your answer (1-4): "))
                options = [question.correctAnswer, question.answer2,
                           question.answer3, question.answer4]
                if options[answer - 1] == question.correctAnswer:
                    self.score += 10
                    print("Correct! +10 points.")
                else:
                    self.lives -= 1
                    print(f"Wrong! You lost a life. {self.lives} remaining.")
            except (IndexError, ValueError):
                print("Invalid input. Please select a number between 1 and 4.")

        print(f"Game over! Your final score: {self.score}")
        self._update_user_score()

    def _update_user_score(self):
        """
        Updates the user's score in the repository after the game ends. 
        The score is added to the user's existing score.

        This method ensures that the score is saved in the repository 
        to maintain persistence across game sessions.
        """
        users = self.user_repo.get_users()
        for user in users:
            if user.username == self.user.username:
                user.score += self.score
        self.user_repo.save_users(users)
        print("Score updated successfully!")
