import asyncio
import aiohttp

class WebScraper(object):
    def __init__(self, urls):
        self.urls = urls
        # Global Place To Store The Data:
        self.all_data  = []
        self.master_dict = {}
        # Run The Scraper:
        asyncio.run(self.main())

    async def fetch(self, session, url):
        try:
            async with session.get(url) as response:
                text = await response.text()
                return text, url
        except Exception as e:
            print(str(e))

    async def main(self):
        tasks = []
        async with aiohttp.ClientSession() as session:
            for url in self.urls:
                tasks.append(self.fetch(session, url))
            htmls = await asyncio.gather(*tasks)
            self.all_data.extend(htmls)

            print(htmls[0][2])
            # Storing the raw HTML data.
            for html in htmls:
                if html is not None:
                    url = html[1]
                    self.master_dict[url] = {'Raw Html': html[0]}
                else:
                    continue

urls = [
        "https://github.com",
        "https://google.com",
        "https://reddit.com",
        "https://nytimes.com",
        "https://producthunt.com",
    ]
scraper = WebScraper(urls = urls)
print(len(scraper.all_data))