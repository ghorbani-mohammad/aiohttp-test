import time
import asyncio
import aiohttp

async def by_aiohttp(total: int):
    # use aiohttp
    async with aiohttp.ClientSession() as session:
        url = "http://httpbin.org/ip"
        for _ in range(total):
            res = await session.get(url)
            print(await res.json())
            
    start_time = time.time()
    asyncio.run(by_aiohttp(total))
    print(f"--- It took {time.time() - start_time} seconds ---")
    
if __name__ == "__main__":
    total = 10
    start_time = time.time()
    asyncio.run(by_aiohttp(total))
    print(f"--- It took {time.time() - start_time} seconds ---")