from enum import StrEnum

from pydantic import BaseModel, Field


class BookSchema(BaseModel):
    title: str = Field(min_length=1, max_length=256)
    author: str = Field(min_length=1, max_length=256)
    year: int | None = Field(ge=0, le=2025)


class BookResponseSchema(BaseModel):
    id: int
    title: str
    author: str
    year: int | None


class BookListResponseSchema(BaseModel):
    books: list[BookResponseSchema]
    pages: int


class SortEnum(StrEnum):
    ASC = "asc"
    DESC = "desc"


class Pagination(BaseModel):
    per_page: int
    page: int
    order: SortEnum
