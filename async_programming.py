import time
import asyncio

async def brew(name):
    print(f"Brewing {name} ...")
    await asyncio.sleep(2)
    # time.sleep(2)
    print(f"{name} is ready")
    
async def some():
    await asyncio.gather(brew("masala"),
    brew("adrak"),
    brew("mint"))

s=time.time()

asyncio.run(some())
# e=time.time()

print(f"Total time is {time.time() - s:.2f}")
