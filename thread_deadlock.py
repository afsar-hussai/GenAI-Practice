import threading

l1=threading.Lock()
l2=threading.Lock()

def task1():
    with l1:
        print("Task 1")
        with l2:
            print("Task 2")

def task2():
    with l2:
        print("Task 2")
        with l1:
            print("Task 1")


# tasks=[threading.Thread(target=task1), threading.Thread(target=task2)  ]

# for n in tasks: n.start()

t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)

t1.start()
t2.start()
