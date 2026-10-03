import uuid
from datetime import datetime, date
from typing import Dict, Any, Optional
from pydantic import BaseModel, ConfigDict, Field


class SiteLogBase(BaseModel):
    log_date: date
    raw_notes: Optional[str] = None
    manpower: Dict[str, Any] = Field(default_factory=dict)
    pour_activities: Dict[str, Any] = Field(default_factory=dict)
    delays_weather: Dict[str, Any] = Field(default_factory=dict)
    quality_issues: Dict[str, Any] = Field(default_factory=dict)


class SiteLogCreate(SiteLogBase):
    project_id: uuid.UUID


class SiteLogResponse(SiteLogBase):
    id: uuid.UUID
    project_id: uuid.UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
