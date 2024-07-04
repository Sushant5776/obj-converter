# from typing import ClassVar
from pydantic import (
    HttpUrl,
    # field_validator,
)
from .data_fields import DataFields


class DescriptionResponse(DataFields):
    id: str
    title: str
    description: str
    imageUrl: HttpUrl

    # MIN_TITLE_LENGTH: ClassVar[int] = 3
    # MAX_TITLE_LENGTH: ClassVar[int] = 64
    # MIN_DESCRIPTION_LENGTH: ClassVar[int] = 32
    # MAX_DESCRIPTION_LENGTH: ClassVar[int] = 128

    # @field_validator("title")
    # @classmethod
    # def title_validator(cls, value: str):
    #     if len(value.strip()) < cls.MIN_TITLE_LENGTH:
    #         raise ValueError(
    #             f"title must be at least {cls.MIN_TITLE_LENGTH} characters long"
    #         )

    #     if len(value.strip()) > cls.MAX_TITLE_LENGTH:
    #         raise ValueError(
    #             f"title cannot be longer than {cls.MAX_TITLE_LENGTH} characters"
    #         )

    #     return value.strip()

    # @field_validator("description")
    # @classmethod
    # def description_validator(cls, value: str):
    #     if len(value.strip()) < cls.MIN_DESCRIPTION_LENGTH:
    #         raise ValueError(
    #             f"description must be at least {cls.MIN_DESCRIPTION_LENGTH} characters long"
    #         )

    #     if len(value.strip()) > cls.MAX_DESCRIPTION_LENGTH:
    #         raise ValueError(
    #             f"description cannot be longer than {cls.MAX_DESCRIPTION_LENGTH} characters"
    #         )

    #     return value.strip()
