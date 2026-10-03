import uuid
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional, TYPE_CHECKING
from sqlalchemy import String, DateTime, ForeignKey, JSON, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.project import Project


class IssueRFI(Base):
    """
    IssueRFI represents field conflicts, drawing discrepancies, and formal Requests for Information (RFI).
    Ensures zero invented engineering decisions; produces traceable, auditable issue records.
    """
    __tablename__ = "issues_rfis"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    project_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("projects.id", ondelete="CASCADE"), index=True, nullable=False
    )
    rfi_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    location_grid: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    affected_elements: Mapped[List[str]] = mapped_column(JSON, default=list)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    severity: Mapped[str] = mapped_column(String(50), default="MEDIUM")  # CRITICAL, HIGH, MEDIUM, LOW
    status: Mapped[str] = mapped_column(String(50), default="OPEN")  # OPEN, SUBMITTED, RESOLVED, CLOSED
    drawing_references: Mapped[List[str]] = mapped_column(JSON, default=list)
    proposed_solutions: Mapped[List[Dict[str, Any]]] = mapped_column(JSON, default=list)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    # Relationships
    project: Mapped["Project"] = relationship("Project", back_populates="issues_rfis")
