import asyncio
import time
from threading import Thread as th

def logging(data):
    while True:
        print(f"Logging data {data} started...")
        time.sleep(2)
        print(f"Logging data {data} Ended")

async def just_main_process():
    print("Async thread started...")
    await asyncio.sleep(2)
    print("Async thread Ended")

th(target=logging,args=(5,),daemon=True).start()

asyncio.run(just_main_process())