# Creating a speed test decorator
from functools import wraps
from time import time

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"Time Elapsed: {t2 - t1}")
        return result
    return wrapper

@speed_test
def sum_nums(nums, msg):
    print(msg)
    return sum(nums)

print(sum_nums((x for x in range(10000000)), "generator"))
print(sum_nums([x for x in range(10000000)], "list"))
