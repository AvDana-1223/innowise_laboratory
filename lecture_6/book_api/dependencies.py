from fastapi import Query

from book_api.models import Session
from book_api.schemas import Pagination, SortEnum


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


def pagination_params(
    page: int = Query(ge=1, required=False, default=1, le=256),
    per_page: int = Query(ge=1, le=100, required=False, default=10),
    order: SortEnum = SortEnum.ASC,
):
    return Pagination(per_page=per_page, page=page, order=order)
