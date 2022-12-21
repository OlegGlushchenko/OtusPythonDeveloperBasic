"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import (
    sessionmaker,
    declarative_base,
    declared_attr,
    relationship,
)
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Text,
    ForeignKey,
)


PG_CONN_URI = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or "postgresql+asyncpg://username:passwd!@localhost/blog"
)
PG_DB_ECHO = True

async_engine: AsyncEngine = create_async_engine(
    url=PG_CONN_URI,
    echo=PG_DB_ECHO,
)

Session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


Base = declarative_base(bind=async_engine, cls=Base)


class User(Base):
    name = Column(String(50), unique=True)
    username = Column(String(20), unique=True)
    email = Column(String(200), unique=True)
    archived = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r})"


class Post(Base):
    user_id = Column(Integer, ForeignKey(User.id), nullable=False, unique=False)
    title = Column(String(200), unique=True)
    body = Column(Text, nullable=False, default="")

    user = relationship("User", back_populates="posts")

    def __str__(self):
        return f"Post(id={self.id}, title={self.title!r}, body={self.body})"
