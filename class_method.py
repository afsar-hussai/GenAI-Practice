class ChaiItems:
    def __init__(self,type_,cost,strength):
        self.type=type_
        self.strength=strength
        self.cost=cost

    @classmethod
    def dict_input(cls,dicti):
        return cls(
            dicti["type"],
            dicti["cost"],
            dicti["strength"]
        )
    @classmethod
    def string_input(cls,text):
        type_,cost,strength=text.split(",")
        return cls(
            type_, cost, strength)


obj1=ChaiItems("adrak",25,"strong")
obj2=ChaiItems.dict_input({
    "type":"elaichi",
    "cost":55,
    "strength":"medium"
    })

text2="masala,44,low"
obj3=ChaiItems.string_input(text2)

print(f"type={obj1.type} cost={obj1.cost} strength={obj1.strength}")
print(f"type={obj2.type} cost={obj2.cost} strength={obj2.strength}")
print(f"type={obj3.type} cost={obj3.cost} strength={obj3.strength}")