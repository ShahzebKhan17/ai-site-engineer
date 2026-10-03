import uuid
from datetime import datetime, date
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, ConfigDict, Field


class DocumentBase(BaseModel):
    doc_category: str = Field(..., description="structural, architectural, boq, bbs, spec, dpr")
    drawing_number: Optional[str] = Field(None, description="Drawing identifier e.g., DWG-STR-COL-02")
    revision: str = Field("Rev 0", description="Document revision code e.g. Rev 0, Rev 1")
    revision_date: Optional[date] = None
    discipline: str = Field("Structural", description="Discipline e.g., Structural, Architectural, MEP")
    status: str = Field("APPROVED_FOR_CONSTRUCTION", description="Document approval status")


class DocumentCreate(DocumentBase):
    project_id: uuid.UUID


class DocumentResponse(DocumentBase):
    id: uuid.UUID
    project_id: uuid.UUID
    filename: str
    file_path: str
    file_hash: str
    doc_metadata: Dict[str, Any] = Field(default_factory=dict)
    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ChunkResponse(BaseModel):
    id: uuid.UUID
    document_id: uuid.UUID
    project_id: uuid.UUID
    chunk_index: int
    content: str
    page_number: Optional[int] = None
    sheet_number: Optional[str] = None
    grid_reference: Optional[str] = None
    element_tags: List[str] = Field(default_factory=list)
    revision: str
    token_count: int

    model_config = ConfigDict(from_attributes=True)
