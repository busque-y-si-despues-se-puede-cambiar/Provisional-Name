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


class QuestionDAO(BaseModel):
    """
    This class is used to define the data structure related to questions.
    """
    statement: str
    category: str
    correctAnswer: str
    answer2: str
    answer3: str
    answer4: str


class QuestionRepository:
    """
    This class represents the behavior of a repository to handle questions data.
    """

    def __init__(self):
        """
        Initialize the class and load questions data from file.
        """
        env = EnvironmentVariables()
        path_file = env.path_questions_data
        self._load_data(path_file)

    def _load_data(self, path_file: str):
        """
        Load questions from JSON file.
        """
        try:
            with open(path_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            if "questions" in data and isinstance(data["questions"], list):
                self.data = data["questions"]
            else:
                print("ERROR: Invalid JSON format, 'questions' key missing or incorrect.")
                self.data = []

        except Exception as e:
            print(f"ERROR loading questions: {e}")
            self.data = []

    def get_questions(self) -> List[QuestionDAO]:
        """
        This method is used to get all questions.
        """
        questions = []
        for question in self.data:
            question_temp = QuestionDAO(
                statement=question["statement"],
                category=question["category"],
                correctAnswer=question["correctAnswer"],
                answer2=question["answer2"],
                answer3=question["answer3"],
                answer4=question["answer4"],
            )
            questions.append(question_temp)
        return questions
