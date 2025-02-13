"""
This module defines the API routes related to the questions.
FastAPI tools are used to expose endpoints.

Authors: 
Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>
Tito Alejandro Burbano Plazas <taburbanop@udistrital.edu.co>
"""

from typing import List
from fastapi import APIRouter, HTTPException
from ..services.question import QuestionServices
from ..repositories.question import QuestionDAO
from ..repositories.user import UserRepository

router = APIRouter()

# Se crea una instancia de UserRepository para pasarla a los servicios
user_repo = UserRepository()
services = QuestionServices(user_repo)

@router.get("/questions/all", response_model=List[QuestionDAO])
def get_all() -> List[QuestionDAO]:
    """
    Retrieve all questions stored in the database.

    Returns:
        List[QuestionDAO]: A list of all questions.
    """
    return services.get_all()

@router.get("/questions/by_keyword/{keyword}", response_model=List[QuestionDAO])
def get_by_keyword(keyword: str) -> List[QuestionDAO]:
    """
    Retrieve questions that match the given keyword in their statement.

    Args:
        keyword (str): The keyword to search for.

    Returns:
        List[QuestionDAO]: A list of matching questions.

    Raises:
        HTTPException: If the keyword is empty.
    """
    if not keyword:
        raise HTTPException(status_code=400, detail="The keyword cannot be empty.")
    return services.get_by_keyword(keyword)

@router.get("/questions/by_category/{category}", response_model=List[QuestionDAO])
def get_by_category(category: str) -> List[QuestionDAO]:
    """
    Retrieve questions that belong to a specific category.

    Args:
        category (str): The category to filter by.

    Returns:
        List[QuestionDAO]: A list of matching questions.

    Raises:
        HTTPException: If the category is empty.
    """
    if not category:
        raise HTTPException(status_code=400, detail="The category cannot be empty.")
    return services.get_by_category(category)

@router.post("/questions/add")
def add_question(question: QuestionDAO):
    """
    Add a new question to the database if the online user is an administrator.

    Args:
        question (QuestionDAO): The question data to be added.

    Returns:
        dict: A success message if the question is added successfully.

    Raises:
        HTTPException: If the online user is not an admin.
    """
    result = services.add_question(question)
    if "error" in result:
        raise HTTPException(status_code=403, detail=result["error"])
    return result
