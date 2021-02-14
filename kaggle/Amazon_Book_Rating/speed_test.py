# Use decorator's concept to spped test the executed function.

from functools import wraps
from time import time

def speed_test(fn):
    
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print("Executing {}".format(fn.__name__))
        print("Time Elapsed: {}".format(end_time - start_time))
        return result
    
    return wrapper


    