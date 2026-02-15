from pydantic import BaseModel, Field

class Blog_post(BaseModel):
    author: str = Field(
        ...,
        max_length=30,
        min_length=3,
        desc="Some Description",
        example="Ashu ji ki karre ho"
    )
    price: float = Field(
        ...,
        ge=300,
        le=1000
    )
    
b1=Blog_post(author="Ashu",price=657)
print(b1)