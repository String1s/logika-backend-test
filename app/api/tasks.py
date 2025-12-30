from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.deps import get_db
from app.core.auth import get_current_user
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.services import task_service

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
    dependencies=[Depends(get_current_user)]
)

@router.post("/", response_model=TaskResponse, status_code=201)
def create(data: TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task(db, data)

@router.get("/", response_model=List[TaskResponse])
def list_tasks(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),
):
    skip = (page - 1) * page_size
    return task_service.get_tasks(db, skip, page_size)

@router.get("/{task_id}", response_model=TaskResponse)
def get(task_id: int, db: Session = Depends(get_db)):
    task = task_service.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskResponse)
def update(task_id: int, data: TaskUpdate, db: Session = Depends(get_db)):
    task = task_service.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_service.update_task(db, task, data)

@router.delete("/{task_id}", status_code=204)
def delete(task_id: int, db: Session = Depends(get_db)):
    task = task_service.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task_service.delete_task(db, task)
