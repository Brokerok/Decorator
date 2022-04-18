import time
from functools import wraps


def decorator(f):
    @wraps(f)
    def answer_f(*args, **kwargs):
        t = time.monotonic()
        return_f = f(*args, **kwargs)
        print(time.monotonic() - t)
        return return_f
    return answer_f


@decorator
def say_hello():
    print('Hello')
