print("Hello")

class A:
    x=6 #field variable
    def __init__(self, par):
        self.par = par

    def display(self):
        print(f"Value: {self.par} and x is {self.x}")

a=A(5)
a.display()
print(a.x)