from sys import getsizeof
def list_chai():
    yield "chai"
    yield "chai latte"
    yield "dirty chai"
    yield "iced chai"

value=list_chai()
print(value)

print(next(value))
print(next(value))  


list1=[ x for x in range(10000000)]
list2=(x for x in range(10000000))

print("List size:", getsizeof(list1))
print("Generator size:", getsizeof(list2))