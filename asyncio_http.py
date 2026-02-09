import asyncio
import aiohttp
import time



async def fetch_url(session,url):
    async with session.get(url) as response:
        print(f"fetched url {url} with status {response.status}")
    
async def main():
    urls=['https://httpbin.org/delay/2']*3
    async with aiohttp.ClientSession() as session:
        tasks=[fetch_url(session,url) for url in urls]
        await asyncio.gather(*tasks)

s=time.time()
asyncio.run(main())

print(f"total time: {time.time()- s:.2f}")