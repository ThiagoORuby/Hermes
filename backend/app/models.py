from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from services.db import Base, engine


class BaseTable(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(
        sa.Integer, primary_key=True, autoincrement=True
    )


class Post(BaseTable):
    __tablename__ = 'posts'

    image_url: Mapped[str]
    title: Mapped[str]
    url: Mapped[str]
    description: Mapped[str]
    datetime: Mapped[str]
    type: Mapped[Optional[str]]


Base.metadata.create_all(engine)
