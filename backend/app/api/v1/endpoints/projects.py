import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectResponse, ProjectUpdate

router = APIRouter()


@router.post("/", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED, summary="Create a new construction project")
def create_project(payload: ProjectCreate, db: Session = Depends(get_db)):
    """Create a new construction project to isolate drawings, documents, and calculations."""
    existing = db.query(Project).filter(Project.code == payload.code).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Project with code '{payload.code}' already exists.",
        )

    project = Project(
        code=payload.code,
        name=payload.name,
        client=payload.client,
        location=payload.location,
        primary_standard=payload.primary_standard,
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


@router.get("/", response_model=List[ProjectResponse], summary="List all construction projects")
def list_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve all construction projects with pagination."""
    return db.query(Project).order_by(Project.created_at.desc()).offset(skip).limit(limit).all()


@router.get("/{project_id}", response_model=ProjectResponse, summary="Get project by ID")
def get_project(project_id: uuid.UUID, db: Session = Depends(get_db)):
    """Retrieve a single project by ID."""
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found.")
    return project
