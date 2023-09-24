from fastapi import FastAPI, HTTPException

from .models import Greeting, GreetingBuilder

app = FastAPI()
storage = {}


@app.get("/")
async def hello(receiver: str = "World") -> Greeting:
    return Greeting.from_receiver(receiver)


@app.post("/greetings/")
async def create_greeting(body: GreetingBuilder) -> Greeting:
    greeting = Greeting.from_builder(body)
    storage[greeting.id] = greeting
    return greeting


@app.get("/greetings/{id}")
async def get_greeting(id) -> Greeting:
    if id not in storage:
        raise HTTPException(status_code=404, detail=f"Greetgng {id} not found")
    return storage[id]
