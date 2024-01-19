import concurrent.futures
from util import logger
import queue
import random
import threading
import time

"""
section 1
Multithreading - Thread(5) - Producer vs Consumer Using Queue
Keyword - 생산자 소비자 패턴
"""

"""
Producer-Consumer Pattern
(1). 멀티스레드 디자인 패턴의 정석
(2). 서버측 프로그래밍의 핵심
(3). 주로 허리역할 중요

Python Event 객체
(1). Flag 초기값 = 0
(2). Set() -> Flag = 1 / Clear() -> Flag = 0 / Wait(1->리턴, 0->대기) / isSet() -> 현 플래그 상태 return
"""

# 생산자
def producer(queue, event):
    # 네트워크 대기 상태 가정(서버)
    while not event.is_set():
        message = random.randint(1, 11)
        logger.info(f'Producer send message : {message}')
        queue.put(message)

    logger.info(f'Producer receive event. Exiting')


# 소비자
def consumer(queue, event):
    # 응답 받고 소비하는 것으로 가정 or DB 저장
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logger.info(f'Consumer storing message : {message} (size={queue.qsize()})')

    logger.info(f'Consumer receive event. Exiting')


if __name__ == '__main__':
    # 큐 사이즈가 매우 중요
    pipline = queue.Queue(maxsize=10)

    # 이벤트 플래그 초기값 = 0
    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipline, event)
        executor.submit(consumer, pipline, event)

        # 실행 시간 조정
        time.sleep(10)

        logger.info("Main : about to set event")

        # 프로그램 종료
        event.set()