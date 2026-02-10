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
    t1=threading.Thread(target=race)
    t2=threading.Thread(target=race)
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print(f"Counter value is : {counter}")