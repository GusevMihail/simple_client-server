import aiohttp
import asyncio
# import threading
import time

# ServerUrl = 'http://127.0.0.1:8080'
ServerUrl = 'http://10.28.11.58:8080'

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, ServerUrl)
        print(html)


def RunClientSession(l):
    l.run_until_complete(main())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # RunClientSession(loop)
    # RequestTimer = threading.Timer(3.0, RunClientSession(loop))
    for i in range(5):
        print (i)
        time.sleep(3.0)
        RunClientSession(loop)
        # RequestTimer.start()
