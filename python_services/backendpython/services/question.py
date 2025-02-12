"""
This module contains the `QuestionServices` class, which is responsible 
for providing services related to questions.

Authors: 
Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>
Tito Alejandro Burbano Plazas <taburbanop@udistrital.edu.co>
"""

from typing import List
from ..repositories.question import QuestionRepository, QuestionDAO


class QuestionServices:
    """
    This class provides services related to questions, such as 
    searching questions by various criteria.
    
    It interacts with the 'QuestionRepository' class to fetch and manage questions.
    """

    def __init__(self):
        """
        Initializes the QuestionServices class and sets up 
        the connection to the `QuestionRepository`.
        """
        self.repository = QuestionRepository()

    def get_all(self) -> List[QuestionDAO]:
        """
        Retrieves all questions from the repository.

        This method fetches every question available in the repository,
        returning them in the form of a list.

        Returns:
            List[QuestionDAO]: A list containing all questions fetched from the repository.
        """
        return self.repository.get_questions()

    def get_by_keyword(self, statement: str) -> List[QuestionDAO]:
        """
        Searches for questions that contain a specific keyword in their statement.

        Args:
            statement (str): The keyword or phrase to search for in the question's statement.

        Returns:
        List[QuestionDAO]: A list of questions where the statement contains the provided keyword.
        """
        response = []
        for question in self.repository.get_questions():
            if statement.lower() in question.statement.lower():
                response.append(question)
        return response

    def get_by_category(self, category: str) -> List[QuestionDAO]:
        """
        Filters questions based on the category they belong to.

        Args:
            category (str): The category to filter questions by.

        Returns:
            List[QuestionDAO]: A list of questions that match the specified category.
        """
        response = []
        for question in self.repository.get_questions():
            if category.lower() in question.category.lower():
                response.append(question)
        return response
