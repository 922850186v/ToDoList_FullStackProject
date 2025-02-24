import datetime
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated, Optional
import models
from databse import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods, including OPTIONS
    allow_headers=["*"],  # Allow all headers
)

models.Base.metadata.create_all(bind=engine)

class TaskBase(BaseModel):
    task_title : str
    task_description : str
    is_done: bool = False
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/api/v1/task/add", status_code=status.HTTP_201_CREATED)
async def add_task(task: TaskBase, db: db_dependency):
        
    db_task = models.Task(
        task_title = task.task_title,
        task_description = task.task_description,
        created_at = datetime.datetime.now(),
        updated_at = datetime.datetime.now()
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Error Adding the Task. Please try again!"
        )
    response = {"result":
                {   
                    f"StatusCode": 201,
                    "Response" : f"Task {db_task.task_title} is Added Successfully!"
                }}
    return response

@app.get("/api/v1/task/get/all", status_code=status.HTTP_200_OK)
async def get_all_tasks( db: db_dependency):
    tasks = db.query(models.Task).order_by(models.Task.created_at.desc()).all()
    response = {"result": []}
    for task in tasks:
        result = {
                "id" : task.id,
                "task" : task.task_title,
                "description" : task.task_description,
                "is_done" : task.is_done
            }
        response["result"].append(result)
    return response
 
 
@app.get("/api/v1/task/get/pending-tasks", status_code=status.HTTP_200_OK)
async def get_pending_tasks( db: db_dependency):
    tasks = db.query(models.Task).filter(models.Task.is_done==False).order_by(models.Task.created_at.desc()).limit(5).all()
    response = {"result": []}
    for task in tasks:
        result = {
                "id" : task.id,
                "task" : task.task_title,
                "description" : task.task_description,
                "is_done" : task.is_done
            }
        response["result"].append(result)
    return response


@app.put("/api/v1/task/update/{task_id}" , status_code=status.HTTP_200_OK)
async def update_task(task_id: int, task: TaskBase, db: db_dependency):
    get_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    
    if not get_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with Id {task_id} is not available"
        )
    else:
        get_task.is_done = task.is_done
        get_task.updated_at = datetime.datetime.now()
        
    db.commit()
    db.refresh(get_task)
    response = {"result":
                {   f"StatusCode": 200,
                    "Response" : f"Task {get_task.task_title} is Updated Successfully!"
                 }}
    return response