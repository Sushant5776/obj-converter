from pydantic import BaseModel, HttpUrl


class DataFields(BaseModel):
    url: HttpUrl
    sku: str
    price: str
    size: str
    brand: str
    images: list[HttpUrl]
