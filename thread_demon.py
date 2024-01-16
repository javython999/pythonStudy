import threading
import logger


"""
section 1
Multithreading - Thread(2) - demon, join
Keyword - DemonThread, Join
"""

"""
DemonThread
(1). 백그라운드에서 실행
(2). 메인쓰레드 종료시 즉시 종료
(3). 주로 백그라운드 무한 대기 이벤트 발생 실행하는 부분 담당 -> JVM(GC), WordProcess(자동저장)
"""

# thread에서 실행 할 함수
def thread_function(name, job):
    logger.info(f"Sub-Thread {name}: starting")

    for i in job:
        print(i)

    logger.info(f"Sub-Thread {name}: finish")


# 메인
if __name__ == "__main__":
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logger.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logger.info("Main-Thread: before creating thread")

    # 함수 인자 확인
    # demon default = False
    thread_1 = threading.Thread(target=thread_function, args=('First', range(2000)), daemon=True)
    thread_2 = threading.Thread(target=thread_function, args=('Second', range(1000)), daemon=True)

    logger.info("Main-Thread: before running thread")

    # thread 시작
    thread_1.start()
    thread_2.start()

    print(thread_1.daemon)
    print(thread_2.daemon)

    # thread join (부모 thread가 자식 thread 종료까지 대기)
    #thread_1.join()
    #thread_2.join()

    logger.info("Main-Thread: wait for the thread to finish")

    logger.info("Main-Thread: all done")