from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str
    is_active:bool

data={'id':25,
      'name':"Ashu",
      "is_active":True
      }

print(f"without pydantics:\n{data}")

user=User(**data)
print(f"with pydantics:\n{user}")
