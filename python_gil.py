"""
section 1
Multithreading - pythons's GIL
Keyword - CPython, memory 관리, GIL 사용이유
"""


"""
GIL(Global Interpreter Lock)
(1). Python 코드를 CPython이 해석(bytecode) 실행시 여러 thread를 사용할 경우 
     단일 thread만이 Python object에 접근하게 제한하는 mutex

(2). CPython의 메모리 관리가 취약(즉 thread-safe)

(3). 단일 thread로도 충분히 빠르다.
(4). process 사용 가능 (Numpy, Scipy)등 GIL 외부 영역에서 효율적인 코딩가능
(5). 병렬 처리는 multi processing, asyncio 등 선택지가 다양함.
(6). thread 동시성 완벽 처리를 위해 -> Jython, IronPython, Stackless Python 등이 존재
"""