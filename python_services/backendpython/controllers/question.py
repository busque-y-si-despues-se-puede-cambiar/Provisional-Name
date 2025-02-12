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

router = APIRouter()

services = QuestionServices()


@router.get("/questions/all")
def get_all() -> List[QuestionDAO]:
    """
    This method is used to obtain all questions.

    This route requires no input parameters and returns a list of 'QuestionDAO' objects, 
    which represent all the questions stored in the database.

    Returns:
        List[QuestionDAO]: List of 'QuestionDAO' objects that contain 
        the information of all questions.
    """
    return services.get_all()


@router.get("/questions/by_keyword/{keyword}")
def get_by_name(keyword: str) -> List[QuestionDAO]:
    """
    This method is used to get questions based on a keyword.

    If the provided keyword is empty, an HTTP exception with code 400 is raised. 
    If the keyword is valid, a list of 'QuestionDAO' objects containing the questions is returned. 
    related to the given keyword.

    Args:
        keyword (str): The keyword by which to filter the questions.

    Returns:
        List[QuestionDAO]: List of 'QuestionDAO' objects containing the questions 
        filtered by the given keyword.
    
    Raises:
        HTTPException: If the keyword is empty, an HTTP 400 exception is thrown.
    """
    if keyword == "":
        raise HTTPException(status_code=400, detail="The keyword cannot be empty.")
    return services.get_by_keyword(keyword)

@router.get("/questions/by_category/{category}")
def get_by_category(category: str) -> List[QuestionDAO]:
    """
    This method is used to obtain questions filtered by category.

    If the provided category is empty, an HTTP exception with code 400 is raised. 
    If the category is valid, a list of 'QuestionDAO' objects containing the questions is returned. 
    belonging to the given category.

    Args:
        category (str): The category by which to filter the questions.

    Returns:
        List[QuestionDAO]: List of 'QuestionDAO' objects containing the questions
        filtered by the given category.
    
    Raises:
        HTTPException: If the category is empty, an HTTP 400 exception is thrown.
    """
    if category == "":
        raise HTTPException(status_code=400, detail="The category cannot be empty.")
    return services.get_by_category(category)
