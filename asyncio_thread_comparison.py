import asyncio
from concurrent.futures import ThreadPoolExecutor
import time

async def item_process(item): ## This is using pure asyncio
    print(f"Processing item {item} ...")
    await asyncio.sleep(3)
    print(f"{item} processed!!")

def fetch_db(item):
    print(f"Fetching data from db {item}")
    time.sleep(3)
    print(f"Data fetched from db {item}")

async def main():
    loop=asyncio.get_running_loop()
    list1=["adrak","elaichi","soya"]
    print("-----Tasks Started--------\n")
    
    with ThreadPoolExecutor() as pool:
        tasks=[loop.run_in_executor(pool,fetch_db,n) for n in list1]
        prcs=asyncio.create_task(item_process("samosa"))
        print("Sare tasks parallel mein chal rahe hain...\n")
        await asyncio.gather(*tasks,prcs)
        
        print("-----Tasks Completed--------\n")
        
        
s=time.time()
asyncio.run(main())
print(f"total time to fetch is {time.time()-s:.2f}")