from pydantic import BaseModel
from typing import List, Dict, Optional

class Product(BaseModel):
    id: int
    items: List[str]
    is_available: bool=True
    spec: Dict[str,str]
    desc:Optional[str]="Good Product"
    
p1=Product(id=56,items=["headphones","mouse","charger"],spec={
    "warranty":"1yr",
    "is water proof":"yes"}
    )
print(p1)


