import multiprocessing
import time

import requests

from util import logger

"""
section 3
Concurrency, CPU Bound, VS I/O Bound - Multiprocessing
Keyword - I/O Bound, Request
"""

# 각 프로세스 메모리 영역에 생성되는 객체(독립적)
# 함수 실행 할 때마다 객체 생성은 좋지 않음 -> 각 프로세스 마다 할당

session = None


def main():
    # test URL
    urls = [
               "https://www.jython.org",
               "http://olympus.realpython.org/dice",
               "https://realpython.com"
           ] * 5

    # 실행시간
    start_time = time.time()

    # 실행
    request_all_sites(urls)

    # 종료
    duration = time.time() - start_time

    # 결과 출력
    logger.info(f'Download {len(urls)} sites in {round(duration, 3)} seconds')


def request_all_sites(urls):
    # 멀티스레드 실행
    # 반드시 processes 개수 조정후 session 객체 확인
    with multiprocessing.Pool(initializer=set_global_session, processes=4) as pool:
        pool.map(request_site, urls)


def request_site(url):
    # session 획득
    logger.info(f'{url}')
    logger.info(f'session : {session}')
    logger.info(f'{session.headers}')

    with session.get(url) as response:
        name = multiprocessing.current_process().name
        logger.info(f'[{name} Read Contents : {len(response.content)} | Status Code : {response.status_code} | from {url}]')


def set_global_session():
    global session
    if not session:
        session = requests.Session()


if __name__ == '__main__':
    main()
