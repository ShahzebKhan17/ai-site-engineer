import uuid
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import String, Integer, Text, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.document import Document


class DocumentChunk(Base):
    """
    DocumentChunk represents discrete chunks extracted from project documents with
    construction-specific tags (grid reference, element tags, revision, sheet).
    """
    __tablename__ = "document_chunks"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    document_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("documents.id", ondelete="CASCADE"), index=True, nullable=False
    )
    project_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("projects.id", ondelete="CASCADE"), index=True, nullable=False
    )
    chunk_index: Mapped[int] = mapped_column(Integer, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    page_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    sheet_number: Mapped[Optional[str]] = mapped_column(String(100), nullable=True, index=True)
    grid_reference: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    element_tags: Mapped[Optional[List[str]]] = mapped_column(JSON, default=list)
    revision: Mapped[str] = mapped_column(String(20), default="Rev 0", index=True)
    token_count: Mapped[int] = mapped_column(Integer, default=0)
    embedding_json: Mapped[Optional[List[float]]] = mapped_column(JSON, nullable=True)

    # Relationships
    document: Mapped["Document"] = relationship("Document", back_populates="chunks")
