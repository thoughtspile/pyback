"""Models for the hello app."""

from uuid import uuid4

from pydantic import BaseModel


class GreetingBuilder(BaseModel):
    """The data to build a greeting."""

    receiver: str


class Greeting(BaseModel):
    """A hello for someone."""

    message: str
    id: str | None = None

    @staticmethod
    def from_builder(builder: GreetingBuilder):
        """Create greeting with random id from the data specified."""
        return Greeting(message=f"Hello, {builder.receiver}", id=str(uuid4()))

    @staticmethod
    def from_receiver(receiver: str):
        """Create anonymous greeting for the receiver."""
        return Greeting(message=f"Hello, {receiver}")
