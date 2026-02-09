import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def getting_from_db(item):
    print(f"fetching {item} from db...")
    time.sleep(3)
    print(f"{item} is 56")

async def main():
    it=["adrak","elaichi","soya"]
    loop=asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        tasks=[loop.run_in_executor(pool,getting_from_db,some) for some in it]
        await asyncio.gather(*tasks)
        
s=time.time()
asyncio.run(main())
print(f"total time to fetch is {time.time()-s:.2f}")
        
        
        