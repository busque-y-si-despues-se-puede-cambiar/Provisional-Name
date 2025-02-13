"""
This module defines the classes and methods to manage question data, 
including its structure and loading from a JSON file.

Authors: 
Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>
Tito Alejandro Burbano Plazas <taburbanop@udistrital.edu.co>
"""

import json
from typing import List
from pydantic import BaseModel
from backendpython.environment_variables import EnvironmentVariables
from ..repositories.user import UserRepository

class QuestionDAO(BaseModel):
    """
    Data model representing a question.
    
    Attributes:
        statement (str): The text of the question.
        category (str): The category of the question.
        correctAnswer (str): The correct answer to the question.
        answer2 (str): The second option.
        answer3 (str): The third option.
        answer4 (str): The fourth option.
    """
    statement: str
    category: str
    correctAnswer: str
    answer2: str
    answer3: str
    answer4: str

class QuestionRepository:
    """
    Repository class to manage question data storage and retrieval.
    """

    def __init__(self, user_repo: UserRepository):
        """
        Initialize the repository, load questions from file, 
        and store a reference to the user repository.
        
        Args:
            user_repo (UserRepository): Repository to access user data.
        """
        env = EnvironmentVariables()
        self.path_file = env.path_questions_data
        self._load_data()
        self.user_repo = user_repo

    def _load_data(self):
        """
        Load questions from the JSON file.
        """
        try:
            with open(self.path_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.data = data.get("questions", [])
        except FileNotFoundError as e:
            print(f"ERROR loading questions: {e}")
            self.data = []

    def get_questions(self) -> List[QuestionDAO]:
        """
        Retrieve all questions from the repository.

        Returns:
            List[QuestionDAO]: A list of all question objects.
        """
        return [QuestionDAO(**q) for q in self.data]

    def add_question(self, question: QuestionDAO) -> dict:
        """
        Add a new question to the repository if the online user is an admin.

        Args:
            question (QuestionDAO): The question data to be added.

        Returns:
            dict: A dictionary containing a success message or an error message.
        """
        online_user = next((user for user in self.user_repo.get_users() if user.online), None)
        if not online_user:
            return {"error": "No user is online."}
        if not online_user.admin:
            return {"error": "Online user is not an admin."}

        self.data.append(question.model_dump())
        self._save_data()
        return {"success": "Question added successfully."}

    def _save_data(self):
        """
        Save the updated list of questions back to the JSON file.
        """
        try:
            with open(self.path_file, "w", encoding="utf-8") as f:
                json.dump({"questions": self.data}, f, indent=4)
        except FileNotFoundError as e:
            print(f"ERROR saving questions: {e}")
