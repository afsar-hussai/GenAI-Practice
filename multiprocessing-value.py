from multiprocessing import Process, Value

## Value is used to access a storage or memory between multiple processes

# Below is problem

# counter=0

def increament_counter_to_n(n,counter):
    # global counter
    for i in range(n):
        counter.value+=1



if __name__ == "__main__":
    counter=Value('i',0)
    processes=[Process(target=increament_counter_to_n,args=(10,counter)) for _ in range(2)]
    
    [ p.start() for p in processes]
    [ p.join() for p in processes]
    print(f"counter is: {counter.value}")
    