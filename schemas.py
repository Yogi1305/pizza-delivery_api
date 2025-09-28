from pydantic import BaseModel
from typing import Optional

class SignModel(BaseModel):
    id: Optional[int] = None  
    Username: str
    Email: str
    Password: str

    model_config = {
        "from_attributes": True   
    }
