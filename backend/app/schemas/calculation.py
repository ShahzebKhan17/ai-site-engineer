import uuid
from datetime import datetime
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, ConfigDict, Field


class RebarBarInput(BaseModel):
    bar_mark: Optional[str] = Field(None, description="Mark identifier e.g., 01, B1")
    diameter_mm: float = Field(..., gt=0, le=50, description="Nominal diameter in mm (e.g., 8, 10, 12, 16, 20, 25, 32)")
    length_m: float = Field(..., gt=0, description="Cutting length of one bar in meters")
    number_of_bars: int = Field(..., ge=1, description="Quantity / count of bars")
    wastage_percent: float = Field(0.0, ge=0.0, le=20.0, description="Rolling/cutting wastage percentage (typically 3-5%)")


class RebarCalculationRequest(BaseModel):
    project_id: uuid.UUID
    element_id: Optional[str] = Field(None, description="Target member e.g., Column C-12")
    standard: str = Field("IS 1786", description="Governing standard for unit weights")
    bars: List[RebarBarInput] = Field(..., min_length=1)


class ConcreteCalculationRequest(BaseModel):
    project_id: uuid.UUID
    element_id: Optional[str] = Field(None, description="Target element e.g., Footing F-4")
    length_m: float = Field(..., gt=0)
    width_m: float = Field(..., gt=0)
    depth_m: float = Field(..., gt=0)
    grade: str = Field("M25", description="Concrete mix grade e.g., M20, M25, M30")
    wastage_percent: float = Field(2.0, ge=0.0, le=10.0)


class CalculationResponse(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    calculation_type: str
    engineering_standard: str
    input_parameters: Dict[str, Any]
    calculated_results: Dict[str, Any]
    formula_breakdown: str
    verified: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
