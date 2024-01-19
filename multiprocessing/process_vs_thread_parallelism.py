"""
section 2
Parallelism with Multiprocessing - Process vs Theard, Parallelism
Keyword - Process, Thread, 병렬성
"""


"""
Parallelism
    - 완전한 동일한 타이밍(시점)에 task 실행
    - 다양한 파트(부분)으로 나눠서 실행(합을 나눠서 구하고 취합)
    - CPU가 싱글 코어일 경우 멀티프로세싱을 만족하지 않음.

Process vs Theard
    - 독립된 메모리(프로세스), 공유 메모리(스레드)
    - 많은 메모리 필요(프로세스), 적은 메모리(스레드)
    - 좀비(데드)프로세스 생성 가능, 좀비(데드)스레드 생성 쉽지 않음
    - 오버헤드 크다(프로세스), 오버헤드 작다(스레드)
    - 생성과 소멸 다소 느림(프로세스), 생성 소멸이 비교적 빠르다
    - 코드 작성 쉬움/디버깅 어려움(프로세스), 코드 작성이 어려움/디버깅 어려움(스레드)
"""