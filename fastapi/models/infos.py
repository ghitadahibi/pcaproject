from pydantic import BaseModel

class Rec(BaseModel):
    firstName: str
    lastName: str
    cin: str
   
    