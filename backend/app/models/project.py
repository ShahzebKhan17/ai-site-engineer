import uuid
from datetime import datetime, timezone
from typing import List, TYPE_CHECKING
from sqlalchemy import String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.document import Document
    from app.models.calculation import CalculationLog
    from app.models.site_log import SiteLog
    from app.models.issue_rfi import IssueRFI


class Project(Base):
    """
    Project model representing isolated construction job sites.
    All documents, drawings, calculations, and site logs strictly map to a project_id.
    """
    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    code: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    client: Mapped[str] = mapped_column(String(255), nullable=True)
    location: Mapped[str] = mapped_column(String(255), nullable=True)
    primary_standard: Mapped[str] = mapped_column(String(50), default="IS 456 / IS 1786")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    # Relationships
    documents: Mapped[List["Document"]] = relationship(
        "Document", back_populates="project", cascade="all, delete-orphan"
    )
    calculations: Mapped[List["CalculationLog"]] = relationship(
        "CalculationLog", back_populates="project", cascade="all, delete-orphan"
    )
    site_logs: Mapped[List["SiteLog"]] = relationship(
        "SiteLog", back_populates="project", cascade="all, delete-orphan"
    )
    issues_rfis: Mapped[List["IssueRFI"]] = relationship(
        "IssueRFI", back_populates="project", cascade="all, delete-orphan"
    )
