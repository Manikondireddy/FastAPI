from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel
DATABASE_URL = "postgresql://postgres:Mani123%40@localhost:5432/test_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
class Employee(Base):

    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    salary = Column(Numeric(10,2), nullable=False)

Base.metadata.create_all(bind=engine)

class EmployeeCreate(BaseModel):
    name: str
    age: int
    salary: float

class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/employees/", response_model=EmployeeResponse)
def create_employee(emp: EmployeeCreate, db: Session = Depends(get_db)):
    new_emp = Employee(name=emp.name, age=emp.age, salary=emp.salary)
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

# READ ALL
@app.get("/employees/", response_model=list[EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

# READ BY ID
@app.get("/employees/{emp_id}", response_model=EmployeeResponse)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

# UPDATE
@app.put("/employees/{emp_id}", response_model=EmployeeResponse)
def update_employee(emp_id: int, updated: EmployeeCreate, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    emp.name = updated.name
    emp.age = updated.age
    emp.salary = updated.salary

    db.commit()
    db.refresh(emp)
    return emp

# DELETE
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted successfully"}




