import time
import cProfile
from time import sleep
from line_profiler import LineProfiler
from random import randint

def test_func():
    time.sleep(randint(1, 3))
    return True

def profile_with_time():
    start_func = time.time()
    test_func()
    end_func = time.time()
    time_of_exec = end_func - start_func
    print("Time of execution: {}".format(time_of_exec))

profile_with_time()

def profile_with_cProfile():
	cProfile.run('test_func()')

profile_with_cProfile()


#LineProfiler
def do_smt(num):
    s = sum(num)

def smt(num):
    do_smt(num)
    time.sleep(1)
    counter = 0
    x = [num[i] / randint(1, 5) for i in range(len(num))]
    for i in x:
        counter += 1

num = [randint(1, 13) for i in range(14)]
lp = LineProfiler()
lp.add_function(do_smt)
lp_wrapper = lp(smt)
lp_wrapper(num)
lp.print_stats()
