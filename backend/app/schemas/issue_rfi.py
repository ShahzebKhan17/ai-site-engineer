import uuid
from datetime import datetime
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, ConfigDict, Field


class IssueRFIBase(BaseModel):
    rfi_number: str = Field(..., description="Unique RFI reference code e.g., RFI-001")
    title: str = Field(..., min_length=3, max_length=255)
    location_grid: Optional[str] = None
    affected_elements: List[str] = Field(default_factory=list)
    description: str
    severity: str = Field("MEDIUM", description="CRITICAL, HIGH, MEDIUM, LOW")
    status: str = Field("OPEN", description="OPEN, SUBMITTED, RESOLVED, CLOSED")
    drawing_references: List[str] = Field(default_factory=list)
    proposed_solutions: List[Dict[str, Any]] = Field(default_factory=list)


class IssueRFICreate(IssueRFIBase):
    project_id: uuid.UUID


class IssueRFIResponse(IssueRFIBase):
    id: uuid.UUID
    project_id: uuid.UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
