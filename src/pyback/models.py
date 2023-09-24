from uuid import uuid4

from pydantic import BaseModel


class GreetingBuilder(BaseModel):
    receiver: str


class Greeting(BaseModel):
    message: str
    id: str | None = None

    @staticmethod
    def from_builder(builder: GreetingBuilder):
        return Greeting(message=f"Hello, {builder.receiver}", id=str(uuid4()))

    @staticmethod
    def from_receiver(receiver: str):
        return Greeting(message=f"Hello, {receiver}")
