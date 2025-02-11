"""Main module of the project.

Author: Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>
"""

from fastapi import FastAPI

from backendpython.controllers.question import router as question_router
from backendpython.controllers.user import router as user_router

app = FastAPI(
    title="Machines and Videogames",
    description="This project is used to manage machines and videogames.",
    version="0.0.1",
)

app.include_router(question_router)
app.include_router(user_router)