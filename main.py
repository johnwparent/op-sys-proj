from schedule import *
import sys




def main():
    seed = sys.argv[1]
    lamm = sys.argv[2]
    upper_bound = sys.argv[3]
    n = sys.argv[4]
    t_cs = sys.argv[5]
    alpha = sys.argv[6]
    time_slice = sys.argv[7]
    rr_add = sys.argv[8]
    time_val = 0
    ''' initial set of simulations, pre scheduling '''
    process_list = simulation_setup(seed,lamm,upper_bound,n)

    ''' apply all scheduling from here '''

    

if __name__ == '__main__':
    main()
