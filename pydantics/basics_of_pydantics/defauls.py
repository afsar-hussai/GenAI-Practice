from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    in_stock: bool=True
    

# p1=Product(id=34,name="earphones",in_stock=True)
p1=Product(id=34,name="earphones")
print(p1)