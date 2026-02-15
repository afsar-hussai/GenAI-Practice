import time
import threading
counter=0
def race():
    global counter
    local_counter=counter
    time.sleep(0.1)
    local_counter+=1
    counter=local_counter
    
if __name__ == "__main__":
    task=[threading.Thread(target=race) for _ in range(2)]
    for n in task: n.start()
    for n in task: n.join()
    
    print(f"Counter value is : {counter} \nbut expected output is 2")