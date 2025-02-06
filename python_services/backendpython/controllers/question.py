"""This is a module to define some endpoints to handle questions data.

Author: Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>
"""

from typing import List
from fastapi import APIRouter, HTTPException
from services.question import QuestionServices
from repositories.question import QuestionDAO

router = APIRouter()

services = QuestionServices()


@router.get("/questions/all")
def get_all() -> List[QuestionDAO]:
    """This method is used to get all questions."""
    return services.get_all()


@router.get("/questions/by_keyword/{keyword}")
def get_by_name(keyword: str) -> List[QuestionDAO]:
    """This method is used to get questions by a keyword."""
    if keyword == "":
        raise HTTPException(status_code=400, detail="The keyword cannot be empty.")   
    return services.get_by_keyword(keyword)

@router.get("/questions/by_category/{category}")
def get_by_category(category: str) -> List[QuestionDAO]:
    """This method is used to get videogames by category."""
    if category == "":
        raise HTTPException(status_code=400, detail="The category cannot be empty.")
    return services.get_by_category(category)
