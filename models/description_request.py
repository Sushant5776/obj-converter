from .data_fields import DataFields


class DescriptionRequest(DataFields):
    name: str
    description: list[dict[str, str]]
