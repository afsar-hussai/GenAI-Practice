from multiprocessing import Process, Queue

## Value is used to access a storage or memory between multiple processes

# Below is problem

# counter=0

def square_number(n,q):
    summ=0

    for i in n:
        summ+=i*i
    
    q.put(summ)



if __name__ == "__main__":
    q=Queue()
    nums=[1,2,3,4]
    # processes=[Process(target=square_number,args=(nums,q)) for _ in range(2)]
    
    # [ p.start() for p in processes]
    # [ p.join() for p in processes]
    p=Process(target=square_number,args=(nums,q))
    p.start()
    p.join()
    
    while not q.empty():
        
        print(f"queue is: {q.get()}")
    