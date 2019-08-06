import time
from contextlib import contextmanager


@contextmanager
def exec_time():
    start = time.time()
    yield
    end = time.time()
    print(f"this code segment cost time: {end-start}ms")
