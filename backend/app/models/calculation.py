import uuid
from datetime import datetime, timezone
from typing import Dict, Any, TYPE_CHECKING
from sqlalchemy import String, DateTime, Boolean, ForeignKey, JSON, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.project import Project


class CalculationLog(Base):
    """
    CalculationLog stores auditable logs of all deterministic engineering tool runs.
    Ensures zero black-box calculations; every parameter, formula, standard, and breakdown is recorded.
    """
    __tablename__ = "calculation_logs"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    project_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("projects.id", ondelete="CASCADE"), index=True, nullable=False
    )
    calculation_type: Mapped[str] = mapped_column(String(100), nullable=False)  # rebar_weight, concrete_volume, formwork_area, earthwork, brickwork
    engineering_standard: Mapped[str] = mapped_column(String(50), default="IS 1786 / IS 456")
    input_parameters: Mapped[Dict[str, Any]] = mapped_column(JSON, nullable=False)
    calculated_results: Mapped[Dict[str, Any]] = mapped_column(JSON, nullable=False)
    formula_breakdown: Mapped[str] = mapped_column(Text, nullable=False)
    verified: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    # Relationships
    project: Mapped["Project"] = relationship("Project", back_populates="calculations")
