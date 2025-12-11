from typing import Annotated
from math import ceil

import uvicorn
from sqlalchemy import select, func
from fastapi import FastAPI, Depends, HTTPException

from book_api.models import Books, Session
from book_api.dependencies import get_db, pagination_params
from book_api.schemas import (
    BookSchema,
    BookResponseSchema,
    Pagination,
    SortEnum,
    BookListResponseSchema
)

app = FastAPI()


@app.post("/books/")
def create_book(
    book: BookSchema,
    db: Session = Depends(get_db)
) -> BookResponseSchema:
    """
    Create a new book entry.

    This endpoint accepts book data, creates a new `Books` record in the
    database, commits the transaction, and returns the created book object.
    """

    new_book = Books(
        title=book.title,
        author=book.author,
        year=book.year
    )

    db.add(new_book)
    db.commit()

    return new_book


@app.get("/books/")
def list_all_books(
    pagination: Annotated[Pagination, Depends(pagination_params)],
    db: Session = Depends(get_db),
) -> BookListResponseSchema:
    query = (
        select(Books)
        .limit(pagination.per_page)
        .offset(
            pagination.page - 1
            if pagination.page == 1
            else (pagination.page - 1) * pagination.per_page
        )
    )

    if pagination.order == SortEnum.DESC:
        query = query.order_by(Books.id.desc())
    else:
        query = query.order_by(Books.id)

    books = db.execute(query).scalars().all()

    count = db.execute(
        select(func.count()).select_from(select(Books.id).subquery())
    ).scalar_one()

    return BookListResponseSchema(
        books=[book.__dict__ for book in books],
        pages=ceil(count / pagination.per_page)
    )


@app.delete("/books/{book_id}")
def delete_book_by_id(book_id: int, db: Session = Depends(get_db)) -> dict:
    """
       Delete a book by its ID.

       This endpoint searches for a book with the given `book_id`. If the book
       exists, it is removed from the database and a success message is returned.
       If no such book is found, a 404 JSON response is returned.
    """

    book = db.query(Books).filter(Books.id == book_id).first()

    if book is None:
        raise HTTPException(detail="Book Not Found", status_code=404)

    db.delete(book)
    db.commit()

    return {"message": f"Book with id {book_id} deleted successfully"}


@app.put("/books/{book_id}")
def update_book(
    book_id: int,
    put_book: BookSchema,
    db: Session = Depends(get_db)
) -> BookResponseSchema:
    """
    Update an existing book by its ID.

    This endpoint retrieves a book with the specified `book_id` and updates
    its title, author, and publication year using the provided data. If the
    book does not exist, a 404 JSON response is returned.
    """

    book = db.query(Books).filter(Books.id == book_id).first()

    book.title = put_book.title
    book.author = put_book.author
    book.year = put_book.year

    if book is None:
        raise HTTPException(detail="Book Not Found", status_code=404)

    db.commit()

    return book


@app.get("/books/search/")
def get_search_book(
    pagination: Annotated[Pagination, Depends(pagination_params)],
    title: str | None = None,
    author: str | None = None,
    year: int | None = None,
    db: Session = Depends(get_db)
) -> BookListResponseSchema:
    """
    Search for books using optional filters.

    This endpoint allows filtering books by title, author, or publication year.
    All parameters are optional, and multiple filters can be combined. The search
    for `title` and `author` is case-insensitive and uses a partial match.
    """

    query = (
        select(Books)
    )

    if pagination.order == SortEnum.DESC:
        query = query.order_by(Books.id.desc())
    else:
        query = query.order_by(Books.id)

    if title:
        query = query.where(Books.title.ilike(f"%{title}%"))
    if author:
        query = query.where(Books.title.ilike(f"%{author}%"))
    if year:
        query = query.where(Books.year == year)

    count = db.execute(
        select(func.count()).select_from(query.subquery())
    ).scalar_one()

    query = (
        query.limit(pagination.per_page)
        .offset(
            pagination.page - 1
            if pagination.page == 1
            else (pagination.page - 1) * pagination.per_page
        )
    )
    books = db.execute(query).scalars().all()

    return BookListResponseSchema(
        books=[book.__dict__ for book in books],
        pages=ceil(count / pagination.per_page)
    )


if __name__ == '__main__':
    uvicorn.run("book_api.main:app", reload=True)
