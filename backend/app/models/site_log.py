import uuid
from datetime import datetime, date, timezone
from typing import Dict, Any, TYPE_CHECKING
from sqlalchemy import String, DateTime, Date, ForeignKey, JSON, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.project import Project


class SiteLog(Base):
    """
    SiteLog represents structured Daily Progress Reports (DPR), manpower records,
    pour activities, weather interruptions, and concrete plant testing slips.
    """
    __tablename__ = "site_logs"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    project_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("projects.id", ondelete="CASCADE"), index=True, nullable=False
    )
    log_date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    raw_notes: Mapped[str] = mapped_column(Text, nullable=True)
    manpower: Mapped[Dict[str, Any]] = mapped_column(JSON, default=dict)
    pour_activities: Mapped[Dict[str, Any]] = mapped_column(JSON, default=dict)
    delays_weather: Mapped[Dict[str, Any]] = mapped_column(JSON, default=dict)
    quality_issues: Mapped[Dict[str, Any]] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    # Relationships
    project: Mapped["Project"] = relationship("Project", back_populates="site_logs")
