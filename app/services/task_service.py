from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

def create_task(db: Session, data: TaskCreate):
    task = Task(**data.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks(db: Session, skip: int, limit: int):
    return db.query(Task).offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task: Task, data: TaskUpdate):
    for field, value in data.dict(exclude_unset=True).items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task: Task):
    db.delete(task)
    db.commit()
