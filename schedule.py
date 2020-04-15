from rand import *
from math import log,floor,ceil, trunc
import string

def get_next_rand(s, exp_lambda):
    return -log(s) / exp_lambda
def simulation_setup(seedval,exp_lambda, upper_bound, n):
    s = Rand()
    s.srand48(seedval)
    d = dict(enumerate(string.ascii_uppercase, 0))
    for i in range(n):
        process_name = d[i]
        init_p_arrival_t = floor(get_next_rand(exp_lambda,s.drand48()))
        if((init_p_arrival_t)>upper_bound):
            while (init_p_arrival_t) > upper_bound:
                init_p_arrival_t = get_next_rand()
        num_cpu_burst = trunc(100*get_next_rand(exp_lambda,s.drand48()))
        num_cpu_burst+=1
        for j in range(num_cpu_burst):
            cpu_burst_time = ceil(get_next_rand(exp_lambda,s.drand48()))
            if j != num_cpu_burst-1:
                io_burst_time = ceil(get_next_rand(exp_lambda,s.drand48()))

    # return dict of processes obj when hookup is ready

#implement SJF SRT FCFS and RR here after calling setup

