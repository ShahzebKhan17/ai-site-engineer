import uuid
from datetime import datetime, date, timezone
from typing import List, Optional, Dict, Any, TYPE_CHECKING
from sqlalchemy import String, DateTime, Date, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.project import Project
    from app.models.chunk import DocumentChunk


class Document(Base):
    """
    Document model representing uploaded construction files (PDF drawings, BOQ spreadsheets, BBS, specs).
    Tracks revisions, disciplines, drawing numbers, and integrity hashes.
    """
    __tablename__ = "documents"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    project_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("projects.id", ondelete="CASCADE"), index=True, nullable=False
    )
    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(500), nullable=False)
    file_hash: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    doc_category: Mapped[str] = mapped_column(String(100), nullable=False)  # structural, architectural, boq, bbs, spec, dpr
    drawing_number: Mapped[Optional[str]] = mapped_column(String(100), nullable=True, index=True)
    revision: Mapped[str] = mapped_column(String(20), default="Rev 0", index=True)
    revision_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    discipline: Mapped[str] = mapped_column(String(50), default="Structural")  # Structural, Architectural, MEP, Civil
    status: Mapped[str] = mapped_column(String(50), default="APPROVED_FOR_CONSTRUCTION")  # DRAFT, SUPERSEDED, APPROVED_FOR_CONSTRUCTION
    doc_metadata: Mapped[Dict[str, Any]] = mapped_column(JSON, default=dict)
    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    # Relationships
    project: Mapped["Project"] = relationship("Project", back_populates="documents")
    chunks: Mapped[List["DocumentChunk"]] = relationship(
        "DocumentChunk", back_populates="document", cascade="all, delete-orphan"
    )
