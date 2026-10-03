import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class ProjectBase(BaseModel):
    code: str = Field(..., min_length=2, max_length=50, description="Unique project code (e.g., PRJ-METRO-01)")
    name: str = Field(..., min_length=3, max_length=255, description="Project Name")
    client: Optional[str] = Field(None, max_length=255, description="Client or Employer name")
    location: Optional[str] = Field(None, max_length=255, description="Site location / City")
    primary_standard: str = Field("IS 456 / IS 1786", description="Governing civil/structural standard")


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=255)
    client: Optional[str] = Field(None, max_length=255)
    location: Optional[str] = Field(None, max_length=255)
    primary_standard: Optional[str] = None


class ProjectResponse(ProjectBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
