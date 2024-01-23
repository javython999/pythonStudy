import asyncio
import time

import aiohttp

from util import logger

"""
section 3
Concurrency, CPU Bound, VS I/O Bound - Multiprocessing
Keyword - I/O Bound, Request
"""

# 각 프로세스 메모리 영역에 생성되는 객체(독립적)
# 함수 실행 할 때마다 객체 생성은 좋지 않음 -> 각 프로세스 마다 할당


def main():
    # test URL
    urls = [
               "https://www.jython.org",
               "http://olympus.realpython.org/dice",
               "https://realpython.com"
    ] * 5

    # 실행시간
    start_time = time.time()

    # Async 실행
    asyncio.run(request_all_sites(urls))

    # 종료
    duration = time.time() - start_time

    # 결과 출력
    logger.info(f'Download {len(urls)} sites in {round(duration, 3)} seconds')


async def request_all_sites(urls):
    async with aiohttp.ClientSession() as session:
        # 작업 목록
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(request_site(url, session))
            tasks.append(task)

        #print(*tasks)
        #print(tasks)

        await asyncio.gather(*tasks, return_exceptions=True)


async def request_site(url, session):
    async with session.get(url) as response:
        print(url)
        logger.info(f'[Read Contents : {response.content_length} | ok? : {response.ok} | from {url}]')

if __name__ == '__main__':
    main()
