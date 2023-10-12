from datetime import datetime as dt

from sqlalchemy import Boolean, Column, DateTime, Integer

from app.core.db import Base


class AbstractBase(Base):
    __abstract__ = True
