"""FastAPI router module."""
from fastapi import FastAPI, HTTPException

from .models import Greeting, GreetingBuilder

app = FastAPI()
storage = {}


@app.get("/")
async def hello(receiver: str = "World") -> Greeting:
    """Greet someone.

    - **receiver**: Who to greet.
    """
    return Greeting.from_receiver(receiver)


@app.post("/greetings/")
async def create_greeting(body: GreetingBuilder) -> Greeting:
    """Save a greeting for later use.

    - **receiver**: Who to greet.
    """
    greeting = Greeting.from_builder(body)
    storage[greeting.id] = greeting
    return greeting


@app.get("/greetings/{id}")
async def get_greeting(id: str) -> Greeting:
    """Get a previously saved greeting.

    - **id**: ID of the saved greeting from POST /greetings.
    """
    if id not in storage:
        raise HTTPException(status_code=404, detail=f"Greetgng {id} not found")
    return storage[id]
