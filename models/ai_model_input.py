from pydantic import BaseModel


class AIModelInput(BaseModel):
    name: str
    price: str
    size: str
    brand: str
    description: list[dict[str, str]]
