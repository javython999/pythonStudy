import logging
import threading
import time

"""
section 1
Multithreading - Thread(1) - Basic
"""

# thread에서 실행 할 함수
def thread_function(name):
    logging.info(f"Sub-Thread {name}: starting")
    time.sleep(3)
    logging.info(f"Sub-Thread {name}: finish")


# 메인
if __name__ == "__main__":
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")

    # 함수 인자 확인
    thread_1 = threading.Thread(target=thread_function, args=('First',))

    logging.info("Main-Thread: before running thread")

    # thread 시작
    thread_1.start()

    # thread join (부모 thread가 자식 thread 종료까지 대기)
    thread_1.join()

    logging.info("Main-Thread: wait for the thread to finish")

    logging.info("Main-Thread: all done")