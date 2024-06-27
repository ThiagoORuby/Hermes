from datetime import datetime
from typing import Optional

import sqlalchemy as sa
from services.db import Base, engine
from sqlalchemy.orm import Mapped, mapped_column


class BaseTable(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(
        sa.Integer, primary_key=True, autoincrement=True
    )


class Post(BaseTable):
    __tablename__ = 'posts'

    image_url: Mapped[Optional[str]]
    title: Mapped[str]
    url: Mapped[str]
    description: Mapped[str]
    date_published: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=True)
    )
    type: Mapped[Optional[str]]


Base.metadata.create_all(engine)
