import threading
import time

# def order_chai():
#     for i in range(1,4):
        
#         print(f"Ordering chai #{i}")

#     time.sleep(2)

# def brew_chai():
#     for i in range(1,4):

#         print(f"Brewing  chai #{i}")

#     time.sleep(5)

# order_thread=threading.Thread(target=order_chai)
# brew_thread=threading.Thread(target=brew_chai)

# order_thread.start()
# brew_thread.start()

# order_thread.join()
# brew_thread.join()

# Example 2 by gemini

def download_file(file_name):
    print(f"Start Downloading {file_name}")
    
    time.sleep(2)
    print(f"End Downloading {file_name}")



print("--- Starting Sequential Downloads ---")
start_seq = time.time()
for i in range(3):
    download_file(f"Photo_{i}.jpg")
end_seq = time.time()
print(f"Sequential total time: {end_seq - start_seq:.2f} seconds\n")

print("--- Starting Concurrent Downloads ---")
start_con = time.time()
threads=[]
for i in range(3):
    th=threading.Thread(target=download_file,args=(f"Photo_{i}.jpg",))
    threads.append(th)
    th.start()


for t in threads:
    t.join()


end_con = time.time()
print(f"Concurrent total time: {end_con - start_con:.2f} seconds")