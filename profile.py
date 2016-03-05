import time


def time_function(method):
    t1 = time.time()
    res = method()
    print '%2.2f sec' % (time.time() - t1)
    return res
