class A:
    label="A: class"

class B(A):
    label="B: class"

class C(A):
    label="C: class"

class D(B, C):
   pass

cup = D()

print(cup.label)  # Output will be from class B due to MRO
print(D.__mro__)  # Method Resolution Order