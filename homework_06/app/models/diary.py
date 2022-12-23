from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Text, Date

from .database import db

if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class Diary(db.Model):
    id = Column(Integer, primary_key=True)
    date = Column(
        Date,
        nullable=False,
    )
    title = Column(
        String,
        nullable=False,
        default="",
        server_default="",
    )
    text = Column(
        Text,
        nullable=False,
        default="",
        server_default="",
    )

    if TYPE_CHECKING:
        query: Query
