"""
section 3
Concurrency, CPU Bound, VS I/O Bound - What is concurrency
Keyword - concurrency
"""

"""
Councurrency(동시성)
    - CPU 가용성 극대화를 위해 Paralleism의 단점 및 어려움을 소프트웨어(구현)레벨에서 해결하기 위한 방법
    - 싱글코어에서 멀티스레드 패턴으로 작업을 처리
    - 동시 작업에 있어서 일정량 처리 후 다음 작업으로 넘기는 방식
    - 즉, 제어권을 주고 받으며 작업처리를 하는 패턴 병렬적은 아니나 유사한 처리방식
    
Councurrency(동시성) VS Paralleism(병렬성)
    - 동시성 : 논리작, 동시 실행 패턴, 싱글코어, 멀티코어에서 실행가능, 한개의 작업을 공유 처리, 디버깅이 어려움, Mutex, DeadLock
    - 병렬성 : 물리적, 물리적으로 동시 실행, 멀티코어에서 구현 가능, 주로 별개의 작업 처리, 디버깅이 어려움, OpenMP, MPI, CUDA
    
"""