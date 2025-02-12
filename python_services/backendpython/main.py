"""
Main module of the project.

Authors:
Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>
Tito Alejandro Burbano Plazas <taburbanoo@udistrital.edu.co>
"""

from fastapi import FastAPI

from backendpython.controllers.question import router as question_router
from backendpython.controllers.user import router as user_router
from backendpython.controllers.game import router as game_router

app = FastAPI(
    title="Machines and Videogames",
    description="This project is used to manage machines and videogames.",
    version="0.0.1",
)

app.include_router(question_router)
app.include_router(user_router)
app.include_router(game_router)
