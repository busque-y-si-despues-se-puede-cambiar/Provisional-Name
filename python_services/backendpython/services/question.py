"""
This module contains the QuestionServices class, which is responsible 
for providing services related to questions.

Authors: 
Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>
Tito Alejandro Burbano Plazas <taburbanop@udistrital.edu.co>
"""

from typing import List
from ..repositories.question import QuestionRepository, QuestionDAO
from ..repositories.user import UserRepository

class QuestionServices:
    """
    Service class for managing question-related operations.
    """

    def __init__(self, user_repo: UserRepository):
        """
        Initialize the service with a reference to the question repository.
        
        Args:
            user_repo (UserRepository): Repository to access user data.
        """
        self.repository = QuestionRepository(user_repo)

    def get_all(self) -> List[QuestionDAO]:
        """
        Retrieve all questions.

        Returns:
            List[QuestionDAO]: A list containing all questions.
        """
        return self.repository.get_questions()

    def get_by_keyword(self, keyword: str) -> List[QuestionDAO]:
        """
        Retrieve questions that contain the given keyword in their statement.

        Args:
            keyword (str): The keyword to search for.

        Returns:
            List[QuestionDAO]: A list of matching questions.
        """
        return [
            question
            for question in self.repository.get_questions()
            if keyword.lower() in question.statement.lower()
        ]

    def get_by_category(self, category: str) -> List[QuestionDAO]:
        """
        Retrieve questions that belong to the given category.

        Args:
            category (str): The category to filter by.

        Returns:
            List[QuestionDAO]: A list of matching questions.
        """
        return [
            question
            for question in self.repository.get_questions()
            if category.lower() in question.category.lower()
        ]

    def add_question(self, question: QuestionDAO) -> dict:
        """
        Add a new question using the repository's add_question method, 
        if the online user is an admin.

        Args:
            question (QuestionDAO): The question data to be added.

        Returns:
            dict: A dictionary with a success message or an error message.
        """
        return self.repository.add_question(question)
