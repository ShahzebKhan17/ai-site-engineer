import uuid
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class RAGQueryRequest(BaseModel):
    project_id: uuid.UUID
    query: str = Field(..., min_length=2, description="Natural language engineering question")
    revision: Optional[str] = Field(None, description="Target revision or defaults to latest approved")
    discipline: Optional[str] = Field(None, description="Filter by discipline (Structural, Architectural, MEP)")
    top_k: int = Field(5, ge=1, le=20)


class CitationSource(BaseModel):
    document_id: uuid.UUID
    filename: str
    drawing_number: Optional[str] = None
    sheet_number: Optional[str] = None
    revision: str
    page_number: Optional[int] = None
    grid_reference: Optional[str] = None
    snippet: str


class RAGQueryResponse(BaseModel):
    project_id: uuid.UUID
    query: str
    answer: str
    citations: List[CitationSource] = Field(default_factory=list)
    calculation_performed: bool = False
    calculation_details: Optional[Dict[str, Any]] = None
    engineering_warning: Optional[str] = None
