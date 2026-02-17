# schemas.py: defines request and response format
from pydantic import BaseModel   # BaseModel is used to create data models.
# pydantic: library used in fastAPI for data validation 
class EmployeeCreate(BaseModel):
    name: str
    email: str 



