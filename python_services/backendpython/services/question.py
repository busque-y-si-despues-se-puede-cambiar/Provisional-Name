"""This module is used to handle services related to questions.

Author: Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>
"""

from typing import List
from ..repositories.question import QuestionRepository, QuestionDAO


class QuestionServices:
    """This class has the services for question searches."""

    def __init__(self):
        self.repository = QuestionRepository()

    def get_all(self) -> List[QuestionDAO]:
        """This method is used to get all questions.

        Returns:
            A list of questions.
        """
        return self.repository.get_questions()

    def get_by_keyword(self, statement: str) -> List[QuestionDAO]:
        """This method is used to get questions by keyword.

        Args:
            keyword (str): The keyword to be searched in the statement of the question.

        Returns:
            A list of questions with the keyword.
        """
        response = []
        for question in self.repository.get_questions():
            if statement.lower() in question.statement.lower():
                response.append(question)
        return response

    def get_by_category(self, category: str) -> List[QuestionDAO]:
        """This method is used to get questions by category.

        Args:
            category (str): The category of the question.

        Returns:
            A list of questions with the category.
        """
        response = []
        for question in self.repository.get_questions():
            if category.lower() in question.category.lower():
                response.append(question)
        return response
