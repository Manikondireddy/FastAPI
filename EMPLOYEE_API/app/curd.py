
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas
from .database import engine, SessionLocal, Base  

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:              
        db.close()


# Create Employee
@app.post("/employees", response_model=schemas.EmployeeCreate)
def create_employees(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = models.Employee(name=employee.name, email=employee.email)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee


# Get All Employees 
@app.get("/employees", response_model=List[schemas.EmployeeCreate])
def get_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()


# Update Employee
@app.put("/employees/{id}", response_model=schemas.EmployeeCreate)
def update_employee(id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == id).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    emp.name = employee.name
    emp.email = employee.email
    db.commit()
    db.refresh(emp)
    return emp


# Delete Employee
@app.delete("/employees/{id}")
def delete_employee(id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == id).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(emp)
    db.commit()
    return {"message": "Deleted successfully"}




