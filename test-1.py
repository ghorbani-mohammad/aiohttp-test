import asyncio
from aiohttp import ClientSession


def fetch_async(urls):
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(fetch_all(urls))
    loop.run_until_complete(future)


async def fetch_all(urls):
    tasks = []
    async with ClientSession() as session:
        for url in urls:
            task = asyncio.ensure_future(fetch(url, session))
            tasks.append(task)
        _ = await asyncio.gather(*tasks)


async def fetch(url, session):
    async with session.get(url) as response:
        return await response.read()


if __name__ == "__main__":
    urls = [
        "https://github.com",
        "https://google.com",
        "https://reddit.com",
        "https://nytimes.com",
        "https://producthunt.com",
    ]
    fetch_async(urls)
