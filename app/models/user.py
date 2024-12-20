from typing import Optional, List

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import String, ForeignKey, Date

from app.database.database import Base


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    orgStructureoOne: Mapped[str] = mapped_column(String(100))
    funcBlock: Mapped[str] = mapped_column(String(100))
    orgStructureTwo: Mapped[Optional[str]] = mapped_column(String(100))
    orgStructureThree: Mapped[Optional[str]] = mapped_column(String(100))
    orgStructureFour: Mapped[Optional[str]] = mapped_column(String(100))
    post: Mapped[str] = mapped_column(String(50))
    role: Mapped[str] = mapped_column(String(50))
    lastName: Mapped[str] = mapped_column(String(50))
    firstName: Mapped[str] = mapped_column(String(50))
    phone: Mapped[str] = mapped_column(String(11))
    city: Mapped[str] = mapped_column(String(50))
    address: Mapped[str] = mapped_column(String(100))
    orgs: Mapped[List["Status"]] = relationship()


class Status(Base):
    __tablename__ = "status"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("user.id"))
    status_type: Mapped[str] = mapped_column(String(100))
    start_date: Mapped[Date] = mapped_column(Date)
    end_date: Mapped[Date] = mapped_column(Date)
