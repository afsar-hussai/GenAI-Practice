class TeaStall:
    def __init__(self,age):
        self._age=age
    
    @property
    def age(self):
        return self._age+2
    
    @age.setter
    def age(self,age):
        if 1<= age <= 5:
            self._age=age
        else:
            raise ValueError("Age is out of range")
        
age1=TeaStall(3)
print(age1.age)
age1.age=2
print(age1.age)